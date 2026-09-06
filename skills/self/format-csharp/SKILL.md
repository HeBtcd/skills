---
name: format-csharp
disable-model-invocation: true
description: Format C# with compact guards, expressions and types, braced work, grouped members, and verbatim backslash strings.
---

- Put return/throw-only single-statement guards on one unbraced line: `if (cond) return false;`. Put wrapped conditions' bodies on their closing line; separate consecutive guards with a blank line.
- Use expression-bodied single-expression members: `public M Create(...) => new(...);`, `public T P => _field;`.
- Preserve separate private backing fields/public properties, existing all-auto-property layouts, and other-purpose fields.
- Keep chains on one line. A chainable method with one effect and `return this` uses one braced line: `public T M(...) { _scope.Do(...); return this; }`. Return-or-throw may use `return cond ? value : throw new InvalidOperationException();`.
- Use K&R braces and four spaces for loops, `try`/`catch`/`finally`, and branches beyond return/throw; retain `else if` chains.
- Collapse short assignment-only constructors: `public X(A a) { A = a; }`; small enums use one line and trailing comma: `{ A, B, C, }`.
- Pack members sharing staticness, visibility, and kind; separate when any changes. Prefer `#region` groups with shortest accurate noun labels, e.g. `Fields`, `Properties`, `Methods`.
- Use verbatim strings for backslashes.
