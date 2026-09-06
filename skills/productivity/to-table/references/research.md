# Research: To Table

## Question

What established concept describes turning a compressed data structure into a small key-value or tabular view, splitting complex topology into related tables, and using that view as a neutral handoff for numerical design?

## Findings

### 1. The surrounding field is program comprehension and reverse engineering

Reverse-engineering research describes recovering higher-level representations from lower-level program representations. That is the broad field around this method, not the name of the method itself. The proposed skill is narrower: it creates a visible data view for reading, without claiming to recover the original design or runtime semantics. [USENIX, “Introduction to Reverse Engineering”](https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/kruegel/kruegel_html/node1.html)

### 2. Data model recovery is the closest established match

Data model recovery is an established reverse-engineering activity. It can recover a physical schema into logical and conceptual schemas, including schema parts that are implicit in the implementation. It is therefore a good match for exposing hidden fields and relationships. [Data Model Recovery](https://digital.ub.uni-paderborn.de/hsmig/download/pdf/3828)

The match is incomplete. Data model recovery normally aims at a conceptual model and may acquire domain semantics from code, data, and related sources. This skill should stop at a neutral structural projection unless the user asks for interpretation. [Extracting Entity-Relationship Diagrams from a Table-Based Legacy Database](https://www.sciencedirect.com/science/article/pii/S0164121207001781)

### 3. Relational representation supports the table view

CodeTrek represents source code as a relational database with schemas, attributes, and relations, then uses queries to work across those relations. This supports treating compressed program data as related rows and references. The system is a program-analysis and machine-learning representation, not a human reading procedure, so it does not supply the skill's complete name or boundary. [CodeTrek: Flexible Modeling of Code using an Extensible Relational Representation](https://openreview.net/forum?id=WQc075jmBmf)

### 4. Parallel arrays have a named storage shape

Structure of Arrays stores each data member in its own array. A shared position across those arrays therefore gives a natural row/column view for a reader. The shared index remains a storage relation; assigning it domain identity would require separate evidence. [Intel oneAPI, “Layouts”](https://www.intel.com/content/www/us/en/docs/dpcpp-cpp-compiler/developer-guide-reference/2023-1/layouts.html)

### 5. Visualization is a separate, broader mechanism

Data-structure visualization tools display an existing structure to make it easier to inspect. Visualization alone does not require converting the structure into key-value tables, preserving a neutral schema, or splitting a topology by connection keys. [USENIX, “deet: A Desktop Error Elimination Tool”](https://www.usenix.org/publications/library/proceedings/ana97/full_papers/hanson/hanson.html)

## Exact match

No single established term covers all of these behaviors:

- `program comprehension` is too broad;
- `data model recovery` covers hidden schema and relations but can include semantic reconstruction;
- `relational representation` describes a representation, not the reading workflow;
- `structure of arrays` covers one storage layout only;
- `data-structure visualization` covers display, not the KV projection rule.

The exact skill is therefore `not established` as one named thing. `to-table` names the requested output, not a formal method.

## Boundary justified by the sources

The skill should:

- project a given data structure into one small KV table when possible;
- use real fields, indexes, paths, row numbers, values, and references;
- represent parallel arrays as columns when they share a position;
- split a complex topology into the smallest connected tables and state their connection keys;
- preserve names, values, order, nesting, and sentinel values;
- expose values, ranges, units, and relations that are actually present.

It should not:

- infer domain meaning from a structural layout;
- trace execution or reconstruct authoring/lowered/runtime layers;
- redesign the data structure;
- produce balancing or tuning recommendations;
- write the temporary tables into source code or a product deliverable without a separate request.

The numerical-design use is an inference from this boundary: a neutral table makes values and relations easier to hand off, but numerical design still owns interpretation, balance, and tuning.

## Disposition

The current skill boundary is supported. No authoring/lowering/runtime workflow, execution trace, or semantic-recovery duty should be added. The research file is retained here as evidence; it is not required input for ordinary use of the skill.
