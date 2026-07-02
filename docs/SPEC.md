# Draft Hashpath Specification

Status: **draft / work in progress**

## Design principles

1. Keep compact strings compact.
2. Do not encode reader-side facts such as route duration or traffic.
3. Do not invent coordinates.
4. Treat a single Hashsite as a one-step Hashpath.
5. Use directive tokens for spatial meaning.
6. Use payloads for payloads, not as a dumping ground for important spatial semantics.
7. Reader view expands compact strings into human instructions.
8. Editor/AI view helps authors create valid structures without learning all tokens.

## Basic form

A Hashpath begins with a full Hashsite:

```text
#FULLCODE
```

It may be followed by directive segments:

```text
#FULLCODE<label><suffix><label><suffix>...
```

Example:

```text
#7B0055pFERRdZAQ
```

Possible expansion:

```text
Base/destination context: #7B0055
Parking: #7BFERR
Door: #7BZAQ
```

## Draft directive table

| Token | Draft meaning |
|---|---|
| a | area/opposite-corner completer for rectangular zones |
| b | callbox / intercom |
| c | compact payload / code / detail |
| d | door / destination / dropoff |
| e | entrance / elevator / escalator, context dependent |
| g | gate / guardpost |
| h | hazard / physical danger |
| i | information / check-in / reception |
| j | deceptive junction / wrong turn / lookalike turnoff |
| k | key / keybox / cache / hidden object |
| l | lobby / loading / lounge |
| m | meet / pickup / handoff |
| n | no-go / avoid rectangle or area |
| p | parking |
| q | callpoint / checkpoint |
| r | road/route condition, or ramp if context requires; unsettled |
| s | stairs / step / search sector depending context; unsettled |
| t | tare point / trailhead / transfer point; unsettled |
| u | turnaround / U-turn point |
| v | visual cue / recognition descriptor |
| w | washroom / water / waypoint support; unsettled |
| x | exit |
| z | usable zone / general target zone |

## Rectangular zones

A rectangle can be represented as:

```text
<label><corner1>a<corner2>
```

Example:

```text
nFERRaZAQ
```

Expansion: no-go rectangle from #...FERR to #...ZAQ.

## Directed movement / one-way path

Draft operator:

```text
>
```

Example:

```text
jFERR>gZAQ
```

Expansion: wrong/deceptive turn at #...FERR; continue one-way/directed segment to the correct gate at #...ZAQ.

## Road/route condition

Draft:

```text
rDW
```

Possible expansion:

```text
D = dirt
W = washboard
G = gravel
F = floods / seasonal water
M = mud
N = narrow
S = steep
4 = high-clearance / 4WD recommended
L = low clearance
```

## Reader-side enrichment

The reader may compute straight-line distance, walking/driving time, route polyline, Google Maps link, and route-in / route-out buttons. These should not be encoded into the compact Hashpath.

## AI generation rules

AI systems must never invent Hashsites or coordinates, must ask for missing map taps or anchors, should use only approved tokens unless asked to propose an extension, should return compact string plus expanded explanation, should mark uncertain choices as assumptions, and should keep route time/distance out of the compact string.
