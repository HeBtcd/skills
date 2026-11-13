---
name: performance-engineering
disable-model-invocation: true
description: "Model a workload's cost, locate the bottleneck, bound the speedup, and prove the claim. Use when something is too slow or allocation-heavy, when a workload's cost must be estimated before building or changing it, or when a claimed speedup needs evidence."
---

# Performance Engineering

An ordered basis of Things over workload cost modeling, profiling, and optimization. Eight moments, in the order the work meets them.

## 1. Whether: the critical 3%

Donald Knuth, [Structured Programming with go to Statements](https://dl.acm.org/doi/10.1145/356635.356640), Computing Surveys 6:4 (1974), p. 268:

> There is no doubt that the grail of efficiency leads to abuse. Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.

> Yet we should not pass up our opportunities in that critical 3%. A good programmer will not be lulled into complacency by such reasoning, he will be wise to look carefully at the critical code; but only after that code has been identified. It is often a mistake to make a priori judgments about what parts of a program are really critical, since the universal experience of programmers who have been using measurement tools has been that their intuitive guesses fail.

## 2. Magnitude: what each layer costs

Peter Norvig, [Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html#answers), appendix "Answers" (the table later popularized by Jeff Dean):

> Approximate timing for various operations on a typical PC:

>     execute typical instruction        1/1,000,000,000 sec = 1 nanosec
>     fetch from L1 cache memory         0.5 nanosec
>     branch misprediction               5 nanosec
>     fetch from L2 cache memory         7 nanosec
>     Mutex lock/unlock                  25 nanosec
>     fetch from main memory             100 nanosec
>     send 2K bytes over 1Gbps network   20,000 nanosec
>     read 1MB sequentially from memory  250,000 nanosec
>     fetch from new disk location (seek) 8,000,000 nanosec
>     read 1MB sequentially from disk    20,000,000 nanosec
>     send packet US to Europe and back  150 milliseconds = 150,000,000 nanosec

Estimate the workload's cost in these units first: cache, memory, disk, and network differ by orders of magnitude, so the layer the work spends its time in decides everything downstream.

## 3. Load: Little's law

John Little, [Little's law](https://en.wikipedia.org/wiki/Little%27s_law) (1961):

> [...] the long-term average number of customers (L) in a stationary system is equal to the long-term average effective arrival rate (λ) multiplied by the average time that a customer spends in the system (W). Expressed algebraically the law is L=λW.

> The relationship is not influenced by the arrival process distribution, the service distribution, the service order, or practically anything else. In most queuing systems, service time is the bottleneck that creates the queue.

> The result applies to any system, and particularly, it applies to systems within systems.

> mean response time = mean number in system / mean throughput

> Software-performance testers have used Little's law to ensure that the observed performance results are not due to bottlenecks imposed by the testing apparatus.

## 4. Where: the USE method

Brendan Gregg, [The USE Method](https://www.brendangregg.com/usemethod.html):

> For every resource, check utilization, saturation, and errors.

> It's intended to be used early in a performance investigation, to identify systemic bottlenecks.

> It begins by posing questions, and then seeks answers, instead of beginning with given metrics (partial answers) and trying to work backwards.

> **resource**: all physical server functional components (CPUs, disks, busses, ...)  
> **utilization**: the average time that the resource was busy servicing work  
> **saturation**: the degree to which the resource has extra work which it can't service, often queued  
> **errors**: the count of error events

> - CPUs: sockets, cores, hardware threads (virtual CPUs)
> - Memory: capacity
> - Network interfaces
> - Storage devices: I/O, capacity
> - Controllers: storage, network cards
> - Interconnects: CPUs, memory, I/O

> It can be useful to consider some software resources as well, or software imposed limits (resource controls), and see which metrics are possible.

## 5. Path: flame graphs

Brendan Gregg, [Flame Graphs](https://www.brendangregg.com/flamegraphs.html):

> [...] a visualization of hierarchical data that I created to visualize stack traces of profiled software so that the most frequent code-paths can be identified quickly and accurately.

> The x-axis shows the stack profile population, sorted alphabetically (it is not the passage of time), and the y-axis shows stack depth, counting from zero at the bottom. Each rectangle represents a stack frame. The wider a frame is [...] the more often it was present in the stacks. The top edge shows what is on-CPU, and beneath it is its ancestry.

> [...] different types of flame graphs: CPU, AI/GPU, Memory, Off-CPU, Hot/Cold, Differential

## 6. Ceiling: Amdahl's law

Gene Amdahl, [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law) (1967):

> the overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used.

> The Speedupoverall is frequently much lower than one might expect. For instance, if a programmer enhances a part of the code that represents 10% of the total execution time (i.e. Timeoptimized of 0.10) and achieves a Speedupoptimized of 10,000, then Speedupoverall becomes 1.11 which means only 11% improvement in total speedup of the program.

With p the fraction of execution time the change improves and s that part's speedup, the whole task's speedup is bounded by 1 / (1 − p + p/s). Compute the bound before paying for the change.

## 7. Change: data dominates

Rob Pike, [Notes on Programming in C](https://www.lysator.liu.se/c/pikestyle.html) (1989):

> Rule 3. Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy. (Even if n does get big, use Rule 2 first.)

> Rule 4. Fancy algorithms are buggier than simple ones, and they're much harder to implement. Use simple algorithms as well as simple data structures.

> Rule 5. Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming. (See Brooks p. 102.)

## 8. Proof: runs, deviation, bias

Gernot Heiser, [Systems Benchmarking Crimes](https://gernot-heiser.org/benchmarking-crimes.html):

> A fair evaluation of a technique/design/implementation that is supposed to improve performance must actually demonstrate two things:
>
> - Progressive criterion: Performance actually does improve significantly in the area of interest
> - Conservative criterion: Performance does not significantly degrade elsewhere

> In order to indicate significance, it is essential that at least standard deviations are quoted. [...] If in doubt use Student's t-test to check the significance.

> Always do several runs, and check the standard deviation. Watch out for abnormal variance.

> Invert the order of measurements. This helps to identify interference between measurements.

> Run sufficient warm-up iterations which aren't timed.

> Always give complete result, not just ratios (unless the denominator is a standard figure).

> Consider the baseline carefully. Often it is the state-of-the-art solution. Often it is the optimal (or theoretically best) solution or a hardware limit [...] the correct baseline is in some sense an unperturbed system.

> For reproducibility it is essential that the evaluation platform is well-specified, including all characteristics that may influence the results.

Mytkowicz, Diwan, Hauswirth, and Sweeney, [Producing Wrong Data Without Doing Anything Obviously Wrong!](https://research.ibm.com/publications/producing-wrong-data-without-doing-anything-obviously-wrong), ASPLOS 2009:

> [...] changing a seemingly innocuous aspect of an experimental setup can cause a systems researcher to draw wrong conclusions from an experiment.

> [...] measurement bias is significant and commonplace in computer system evaluation. By significant we mean that measurement bias can lead to a performance analysis that either over-states an effect or even yields an incorrect conclusion.

> [...] we describe and demonstrate two methods, one for detecting (causal analysis) and one for avoiding (setup randomization) measurement bias.
