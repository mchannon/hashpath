# Hashsite, Hashpath, and Procedural Geography

## Getting directions is solved. Giving directions still sucks.

Modern maps are excellent at getting a person near a place. They can route from a current location to an address, business, road segment, or coordinate.

But real-world arrival often fails after that.

The hard part is not always: how do I get to the address?

It is: which entrance, which driveway, which gate, which parking area, what code, which door, which path after parking, which turn looks right but is wrong, what if the gate is locked, where is the key, where do I leave the package, where do I meet the person, and where do I exit?

Hashpath exists because **the address is often not the destination**.

## Spatial addressing vs. procedural geography

A compact place code answers: where is it?

A route answers: how do I get near it?

A Hashpath answers: what place-dependent sequence should I follow?

Hashpaths encode **procedural geography**: ordered places, areas, movement constraints, recognition cues, access details, fallback instructions, and physical tasks.

## Hashsite

A Hashsite is a compact spatial code for a place or cell.

Hashsites can be used alone:

```text
#7B66A3MM2
```

A single Hashsite can be treated as a one-step Hashpath.

## Hashpath

A Hashpath extends a starting Hashsite into a compact procedure. It supplements ordinary routing with the real-world details that maps usually omit.

A Hashpath may express gate, guardpost, callbox, callpoint, parking, wrong/deceptive turn, no-go area, road surface, stairs, elevator, door, hidden key, pickup point, recognition cue, fallback instruction, exit, and turnaround.

## Reader view vs. editor view

The sender/author chooses points, labels them, adds details, previews the resulting reader page, and shares the link.

The recipient opens the link and sees a simple, human-readable procedure.

Reader-side enrichments such as walking time, drive time, route polylines, or map links are computed at read time. They should not bloat the compact Hashpath.

## Hashpaths are not just waypoint lists

A useful Hashpath may include points, areas, and movement constraints.

Points include gates, parking, callboxes, doors, hidden keys, pickup points, exits, and turnarounds.

Areas include no-go rectangles, parking zones, search sectors, and pickup zones.

Movement constraints include one-way segments, directed paths, deceptive turns, poor road surfaces, and required ingress/egress.

## AI-guided authoring

The AI agent should act as an interviewer and compiler. It should ask whether the point is parking or destination, whether there is a gate/code/callbox/guard, whether a wrong entrance is nearby, whether the road is one-way, whether the surface is unusual, what to do if access fails, whether there is a hidden key, and whether there is a separate exit.

The AI must not invent coordinates. It should ask the user to tap or confirm exact locations.

## Hosted Hashpaths

The open format should remain free and readable.

The hosted layer can add saved paths, vanity aliases, branded pages, private/sensitive payloads, expiration, analytics, QR codes, creator accounts, paid tours/quests, time-synced steps, and offline cache manifests.

The premium value is not the coordinate grammar. It is persistence, trust, privacy, branding, state, and workflow.

## Core thesis

Hashsite is compact spatial addressing.

Hashpath is procedural geography.

BPS and local Hashsites add local sources of truth for GPS-poor or micro-precision environments.

AI turns messy human directions into structured, shareable, readable instructions.
