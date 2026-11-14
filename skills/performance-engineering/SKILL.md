---
name: performance-engineering
disable-model-invocation: true
description: "Estimate, profile, and verify performance cost. Use when something is too slow or allocation-heavy, when cost must be estimated before building, or when a claimed speedup needs evidence."
---

# Performance Engineering

Five moments, in the order the work meets them: estimate it, find it, bound it, fix it, prove it.

## 1. Back-of-the-envelope calculation

Jeff Dean, [Designs, Lessons and Advice from Building Large Distributed Systems](http://www.cs.cornell.edu/projects/ladis2009/talks/dean-keynote-ladis2009.pdf), LADIS 2009 keynote:

> Important skill: ability to estimate performance of a system design [...] without actually having to build it!

> Numbers Everyone Should Know
>
> L1 cache reference                    0.5 ns
> Branch mispredict                     5 ns
> L2 cache reference                    7 ns
> Mutex lock/unlock                     25 ns
> Main memory reference                 100 ns
> Compress 1K bytes with Zippy          3,000 ns
> Send 2K bytes over 1 Gbps network     20,000 ns
> Read 1 MB sequentially from memory    250,000 ns
> Round trip within same datacenter     500,000 ns
> Disk seek                             10,000,000 ns
> Read 1 MB sequentially from disk      20,000,000 ns
> Send packet CA->Netherlands->CA       150,000,000 ns

> How long to generate image results page (30 thumbnails)? Design 1: Read serially, thumbnail 256K images on the fly [...] 30 seeks * 10 ms/seek + 30 * 256K / 30 MB/s = 560 ms [...] Design 2: Issue reads in parallel: [...] 10 ms/seek + 256K read / 30 MB/s = 18 ms [...] (Ignores variance, so really more like 30-60 ms, probably)

> Write Microbenchmarks! [...] Builds intuition for back-of-the-envelope calculations

Price the design on the envelope before building it.

## 2. Profiling

Russ Cox, [Profiling Go Programs](https://go.dev/blog/pprof), The Go Blog:

> By using Go’s profiling tools to identify and correct specific bottlenecks, we can make the Go loop finding program run an order of magnitude faster and use 6x less memory.

> When CPU profiling is enabled, the Go program stops about 100 times per second and records a sample consisting of the program counters on the currently executing goroutine’s stack. [...] In the `go tool pprof` output, there is a row for each function that appeared in a sample. The first two columns show the number of samples in which the function was running (as opposed to waiting for a called function to return), as a raw count and as a percentage of total samples.

> Now the program is spending most of its time allocating memory and garbage collecting [...] To find out why the garbage collector is running so much, we have to find out what is allocating memory. [...] Now the samples we are examining are memory allocations, not clock ticks.

> Having a garbage-collected language doesn’t mean you can ignore memory allocation issues.

Profile the workload as it actually runs, and let the profile's ranking name the suspect.

## 3. Amdahl's law

Wikipedia, [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law):

> the overall performance improvement gained by optimizing a single part of a system is limited by the fraction of time that the improved part is actually used.

> For instance, if a programmer enhances a part of the code that represents 10% of the total execution time (i.e. Timeoptimized of 0.10) and achieves a Speedupoptimized of 10,000, then Speedupoverall becomes 1.11 which means only 11% improvement in total speedup of the program.

> Assume that a task has two independent parts, A and B. Part B takes roughly 25% of the time of the whole computation. By working very hard, one may be able to make this part 5 times faster, but this reduces the time of the whole computation only slightly. In contrast, one may need to perform less work to make part A perform twice as fast.

Rank candidate fixes by the time-share they touch times the speedup they can win, and take the top of that list.

## 4. Program optimization

Wikipedia, [Program optimization](https://en.wikipedia.org/wiki/Program_optimization):

> When the bottleneck is localized, optimization usually starts with a rethinking of the algorithm used in the program. More often than not, a particular algorithm can be specifically tailored to a particular problem, yielding better performance than a generic algorithm.

> After design, the choice of algorithms and data structures affects efficiency more than any other aspect of the program.

> Frequently, algorithmic improvements can cause performance improvements of several orders of magnitude instead of micro-optimizations, which rarely improve performance by more than a few percent.

> A general technique to improve performance is to avoid work. [...] Another important technique is caching, particularly memoization, which avoids redundant computations.

> After the programmer is reasonably sure that the best algorithm is selected, code optimization can start.

Work top-down on the profiled region: rethink the algorithm and data structure first, then tune lines.

## 5. Measurement bias

Mytkowicz, Diwan, Hauswirth, and Sweeney, [Producing Wrong Data Without Doing Anything Obviously Wrong!](https://users.cs.northwestern.edu/~robby/courses/322-2013-spring/mytkowicz-wrong-data.pdf), ASPLOS 2009:

> Systems researchers often use experiments to drive their work: they use experiments to identify bottlenecks and then again to determine if their optimizations for addressing the bottlenecks are effective. If the experiment is biased then a researcher may draw an incorrect conclusion

> For example, consider a researcher who wants to determine if optimization O is beneficial for system S. If she measures S and S + O in an experimental setup that favors S + O, she may overstate the effect of O or even conclude that O is beneficial even when it is not.

> changing the size (in bytes) of an unused environment variable, can dramatically (frequently by about 33% and once by almost 300%) change the performance of our program [...] computer systems are sensitive: an insignificant and seemingly irrelevant change can dramatically affect the performance of the system.

> experimental setup randomization [...] runs each experiment in many different experimental setups; these experiments result in a distribution of observations which we summarize using statistical methods

Verify the claim across varied setups, and report the distribution across runs, so the effect has had every chance to break.
