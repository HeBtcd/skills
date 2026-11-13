---
name: when-in-rome
disable-model-invocation: true
description: "Match the existing implementations and house style of an established codebase before writing new code in it. Use when adding a feature, function, test, or file, and the question is how this place does things rather than how you would."
---

# When in Rome

An established codebase answers how things are done here before you ask. Eight moments, in the order the work meets them.

## 1. Arrive: the place's custom is the default

Ambrose of Milan's rule, retold by Augustine, [Letter 54 to Januarius](https://www.newadvent.org/fathers/1102054.htm) (A.D. 400), ch. 2:

> [...] there is no better rule for the wise and serious Christian in this matter, than to conform to the practice which he finds prevailing in the Church to which it may be his lot to come. For such a custom, if it is clearly not contrary to the faith nor to sound morality, is to be held as a thing indifferent, and ought to be observed for the sake of fellowship with those among whom we live.

> When I visit Rome, I fast on Saturday; when I am here, I do not fast. On the same principle, do you observe the custom prevailing in whatever Church you come to, if you desire neither to give offense by your conduct, nor to find cause of offense in another's.

## 2. Survey: look at the code around you and determine its style

Google's [Python Style Guide](https://google.github.io/styleguide/pyguide.html), Parting Words:

> BE CONSISTENT.

> If you're editing code, take a few minutes to look at the code around you and determine its style. If they use `_idx` suffixes in index variable names, you should too. If their comments have little boxes of hash marks around them, make your comments have little boxes of hash marks around them too.

> The point of having style guidelines is to have a common vocabulary of coding so people can concentrate on what you're saying rather than on how you're saying it. We present global style rules here so people know the vocabulary, but local style is also important. If code you add to a file looks drastically different from the existing code around it, it throws readers out of their rhythm when they go to read it.

## 3. Vocabulary: name it what the codebase names it

Eric Evans's term, glossed by Martin Fowler, [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html):

> Ubiquitous Language is the term Eric Evans uses in Domain Driven Design for the practice of building up a common, rigorous language between developers and users. This language should be based on the Domain Model used in the software - hence the need for it to be rigorous, since software doesn't cope well with ambiguity.

Evans:

> By using the model-based language pervasively and not being satisfied until it flows, we approach a model that is complete and comprehensible, made up of simple elements that combine to express complex ideas.

## 4. Fence: find the reason before you judge the convention

G. K. Chesterton's fence, [The Thing](https://en.wikiquote.org/wiki/G._K._Chesterton#The_Thing_%281929%29) (1929), "The Drift From Domesticity":

> If you don't see the use of it, I certainly won't let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.

> Some person had some reason for thinking it would be a good thing for somebody. And until we know what the reason was, we really cannot judge whether the reason was reasonable.

## 5. Hierarchy: the nearest convention wins

PEP 8, [A Foolish Consistency is the Hobgoblin of Little Minds](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds):

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

> However, know when to be inconsistent – sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask!

> In particular: do not break backwards compatibility just to comply with this PEP!

> Some other good reasons to ignore a particular guideline:
>
> 1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
> 2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) – although this is also an opportunity to clean up someone else's mess (in true XP style).
> [...]

> Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project.

## 6. Surface: observable behavior is the contract

Hyrum Wright, [Hyrum's Law](https://www.hyrumslaw.com/):

> With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.

> [...] if an interface has enough consumers, they will collectively depend on every aspect of the implementation, intentionally or not. This effect serves to constrain changes to the implementation, which must now conform to both the explicitly documented interface, as well as the implicit interface captured by usage.

## 7. Tooling: let the machine own mechanical style

Effective Go, [Formatting](https://go.dev/doc/effective_go#formatting):

> Formatting issues are the most contentious but the least consequential. People can adapt to different formatting styles but it's better if they don't have to, and less time is devoted to the topic if everyone adheres to the same style.

> If you want to know how to handle some new layout situation, run `gofmt`; if the answer doesn't seem right, rearrange your program (or file a bug about `gofmt`), don't work around it.

Rob Pike, [Go Proverbs](https://go-proverbs.github.io/):

> Gofmt's style is no one's favorite, yet gofmt is everyone's favorite.

## 8. Astonishment: read your addition as the next reader

Wikipedia, [Principle of least astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment), quoting the law's first print formulation (1972) and its textbook version:

> [...] every construct in the system should behave exactly as its syntax suggests. Widely accepted conventions should be followed whenever possible, and exceptions to previously established rules of the language should be minimal.

> [...] a programmer should try to think of the behavior that will least surprise someone who uses the program, rather than that behavior that is natural from knowing the inner workings of the program.

> If a necessary feature has a high astonishment factor, it may be necessary to redesign the feature.

Google's [C++ Style Guide](https://google.github.io/styleguide/cppguide.html), Goals of the Style Guide:

> "Leave a trace for the reader" is a particularly common sub-point of this principle: When something surprising or unusual is happening in a snippet of code [...] leaving textual hints for the reader at the point of use is valuable [...]
