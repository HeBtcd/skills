---
name: show-your-math
disable-model-invocation: true
description: "Show the working behind a number or default: the relation it comes from, each input's bounds, the weakest link, the choice left over. Use when a constant needs defending, an estimate is challenged, or the user asks where a figure came from."
---

# Show Your Math

A defended number is the last step of a chain, and the chain is the defense. Six moments, in the order the work meets them.

## 1. Model: the number is the end of a relation

Wikipedia, [Back-of-the-envelope calculation](https://en.wikipedia.org/wiki/Back-of-the-envelope_calculation):

> A back-of-the-envelope calculation is a rough calculation, typically jotted down on any available scrap of paper such as an envelope. It is more than a guess but less than an accurate calculation or mathematical proof. The defining characteristic of back-of-the-envelope calculations is the use of simplified assumptions.

Wikipedia, [Fermi problem](https://en.wikipedia.org/wiki/Fermi_problem):

> Fermi problems typically involve making justified guesses about quantities and their variance or lower and upper bounds.

> Without a reasonable frame of reference to work from it is seldom clear if a result is acceptably precise or is many degrees of magnitude (tens or hundreds of times) too big or too small. The Fermi estimation gives a quick, simple way to obtain this frame of reference for what might reasonably be expected to be the answer.

For a default, the relation is a budget. Google SRE, [Embracing Risk](https://sre.google/sre-book/embracing-risk/):

> Our goal is to explicitly align the risk taken by a given service with the risk the business is willing to bear. We strive to make a service reliable enough, but no *more* reliable than it needs to be.

> For example, a system that serves 2.5M requests in a day with a daily availability target of 99.99% can serve up to 250 errors and still hit its target for that given day.

For a capacity, the relation is Little's law (Wikipedia, [Little's law](https://en.wikipedia.org/wiki/Little%27s_law)):

> [...] the long-term average number of customers (L) in a stationary system is equal to the long-term average effective arrival rate (λ) multiplied by the average time that a customer spends in the system (W). Expressed algebraically the law is L=λW.

> The result applies to any system, and particularly, it applies to systems within systems.

Write the relation first; the number is whatever the relation leaves undetermined.

## 2. Shape: check the empty relation

Wikipedia, [Dimensional analysis](https://en.wikipedia.org/wiki/Dimensional_analysis):

> Any physically meaningful equation or inequality must have the same dimensions on its left and right sides, a property known as dimensional homogeneity. Checking for dimensional homogeneity is a common application of dimensional analysis, serving as a plausibility check on derived equations and computations.

Wikipedia, [Sanity check](https://en.wikipedia.org/wiki/Sanity_check):

> A sanity check or sanity test is a basic test to quickly evaluate whether a claim or the result of a calculation can possibly be true.

> The point of a sanity test is to rule out certain classes of obviously false results, not to catch every possible error.

> Fermi estimates will often provide insight on the order of magnitude of an expected value.

Run the relation where the answer is already known: units balanced, limiting cases right, order of magnitude sane. Do this before filling it in; a malformed relation wastes every input fed to it.

## 3. Inputs: every term carries provenance and a bound

Wikipedia, [Measurement uncertainty](https://en.wikipedia.org/wiki/Measurement_uncertainty):

> All measurements are subject to uncertainty and a measurement result is complete only when it is accompanied by a statement of the associated uncertainty, such as the standard deviation. By international agreement, this uncertainty has a probabilistic basis and reflects incomplete knowledge of the quantity value.

Mark each input: measured, derived from another relation, or guessed. Give every guess a lower and upper bound. A point value presented without its bound claims knowledge the work does not have.

## 4. Weakest link: the input the answer leans on

Wikipedia, [Propagation of uncertainty](https://en.wikipedia.org/wiki/Propagation_of_uncertainty):

> [...] propagation of uncertainty is the effect of variables' uncertainties on the uncertainty of a function based on them.

Wikipedia, [Sensitivity analysis](https://en.wikipedia.org/wiki/Sensitivity_analysis):

> Sensitivity analysis is the study of how the uncertainty in the output of a mathematical model or system (numerical or otherwise) can be divided and allocated to different sources of uncertainty in its inputs.

> Uncertainty reduction, through the identification of model input that cause significant uncertainty in the output and should therefore be the focus of attention in order to increase robustness.

> For calibration of models with large number of parameters, by focusing on the sensitive parameters.

Push each input's bound through the relation and find the one that moves the answer most. Spend calibration effort on that one; tightening the others buys nothing.

## 5. Choice: what remains is preference

Ronald Howard, [Making Good Decisions](https://hbr.org/podcast/2014/11/making-good-decisions), HBR IdeaCast:

> [...] by representing the decision, including the three major factors– what kind of alternatives do you have, what information do you have, how does what you do change different things, which is uncertain, typically, and we model on uncertainty, and then what are your preferences.

> So something they were not at all initially worried about– a preference issue– turned out to be important. Whereas an information issue about the life of the material turned out to be not very important.

Wikipedia, [Decision analysis](https://en.wikipedia.org/wiki/Decision_analysis):

> uncertainties are represented through probabilities [...] The decision maker's attitude to risk is represented by utility functions

After the relation, the bounds, and the weakest link, what still moves the number is a choice, not a fact. Name it as a choice: the alternatives on the table and the preference it serves. A preference stated as a preference can be argued with; one smuggled in as a derivation cannot.

## 6. Show: the chain a reader can check

Pólya, [How to Solve It](https://en.wikipedia.org/wiki/How_to_Solve_It):

> The plan gives a general outline; we have to convince ourselves that the details fit into the outline, and so we have to examine the details one after the other, patiently, till everything is perfectly clear, and no obscure corner remains in which an error could be hidden.

Wikipedia, [Magic number (programming)](https://en.wikipedia.org/wiki/Magic_number_(programming)):

> The single place where the named variable is declared makes a good place to document what the value means and why it has the value it does.

Wikipedia, [Significant figures](https://en.wikipedia.org/wiki/Significant_figures):

> Spurious digits that arise from calculations resulting in a higher precision than the original data or a measurement reported with greater precision than the instrument's resolution.

Write the number where it lives, followed by its chain: the relation, each input with its bound and provenance, the weakest link, and the choice. Report the digits the chain supports and no more.
