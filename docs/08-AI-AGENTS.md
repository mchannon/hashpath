# 8. AI agents and structured instructions

[README](../README.md) | Prev: [7. App behavior](07-APP-BEHAVIOR.md) | Next: [9. BPS and local truth anchors](09-BPS.md)

---

Hashpath is useful for AI agents because arrival instructions are often semi-structured natural language.

An AI agent can help turn this:

```text
Park in the back lot, use the left gate, code 4729, stairs by the loading dock, second door on the right.
```

into a structured sequence:

```text
parking → gate/code → stairs → door
```

## Agent responsibilities

An AI agent should:

- preserve the user's intent
- keep access details attached to the right step
- distinguish places from instructions
- avoid inventing coordinates
- warn when a step is ambiguous
- preserve fallback instructions
- not expose sensitive access details unnecessarily

## Why structure matters

Structured arrival instructions can be:

- previewed
- translated
- shortened
- printed
- embedded
- validated
- routed step-by-step
- converted into app UI

---

[README](../README.md) | Prev: [7. App behavior](07-APP-BEHAVIOR.md) | Next: [9. BPS and local truth anchors](09-BPS.md)
