# 3. Format and segments

[README](../README.md) | Prev: [2. What a Hashpath is](02-WHAT-IS-A-HASHPATH.md) | Next: [4. Places, steps, and labels](04-PLACES-STEPS-LABELS.md)

---

A Hashpath can be represented as a sequence of compact segments.

A spatial segment may use a full Hashsite-style code or a differential suffix from the previous point.

A non-spatial segment can carry access instructions, codes, notes, or labels.

Example:

```text
#7BGPSDMUTc4729#pFCDCsEN4Ld1T^2
```

Possible breakdown:

| Segment | Meaning |
|---|---|
| `#7BGPSDMUT` | first waypoint / gate |
| `c4729#` | access code |
| `pFCDC` | parking waypoint |
| `sEN4L` | stairs waypoint |
| `d1T^2` | door waypoint, +2m altitude |

The point is not to force every instruction into a sentence. The point is to make arrival procedures compact enough to share and structured enough for software to read.

---

[README](../README.md) | Prev: [2. What a Hashpath is](02-WHAT-IS-A-HASHPATH.md) | Next: [4. Places, steps, and labels](04-PLACES-STEPS-LABELS.md)
