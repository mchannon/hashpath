# Instructions for AI Agents and Crawlers

This document is intended for AI crawlers, custom GPTs, Claude Projects, code agents, and future Hashsite authoring assistants.

## Purpose

Hashsite is a compact spatial addressing system.

Hashpath is a compact, AI-readable format for procedural geography: the ordered places, constraints, access details, recognition cues, and fallback instructions that help a human complete a real-world arrival or physical task.

## High-level instruction

When asked to generate a Hashpath:

1. Read the human instructions.
2. Identify spatial steps, areas, constraints, descriptors, and fallback rules.
3. Do not invent coordinates or Hashsites.
4. Ask for missing grounded points.
5. Use the approved draft token table.
6. Return compact Hashpath, expanded reader text, assumptions, missing information, and optional suggested map taps.

## Never invent locations

If the user says “park behind the brown shed” but provides no Hashsite or map point, do not fabricate one. Ask the user to tap the parking point or provide its Hashsite.

Use placeholders only if explicitly drafting: `#PARKING_POINT`, `#DOOR_POINT`, `#WRONG_DRIVEWAY`.

## Do not encode temporary reader-side facts

Do not encode traffic, estimated walking time, estimated driving time, current weather, route API output, or live business hours unless explicitly a payload/note. Those belong to the reader page or external APIs, not the compact Hashpath.

## Classify input

Classify each direction element as waypoint, area, movement constraint, route condition, descriptor, access payload, fallback, or support point.

## Ask useful follow-up questions

For delivery/access, ask whether the point is parking or final delivery, whether there is a gate/code/guard/callbox, whether a wrong entrance is nearby, whether the path is driving/walking/mixed, what to do if access fails, whether there is a separate exit, whether there is a turnaround, whether the road surface is unusual, and what to recognize at arrival.

For hidden key/property access, ask where the key is, what it unlocks, whether it should be returned, whether the entry door is different from the key location, and whether the person exits the same way.

For grocery/warehouse/tasking, ask for the starting/tare point, target micro-region, expected/verified item location, missing-item behavior, and scan/photo confirmation rules.

## Suggested JSON response format

```json
{
  "assistantMessage": "Tap the wrong driveway first, then the correct gate.",
  "requestedMapTaps": [
    {"role": "wrong_turn", "token": "j", "label": "Wrong/deceptive driveway"},
    {"role": "gate", "token": "g", "label": "Correct gate"}
  ],
  "suggestedQuestions": [
    "Is this road one-way?",
    "Is the surface paved, dirt, gravel, washboard, muddy, or seasonal?",
    "What should the recipient do if the gate is locked?"
  ],
  "draftHashpath": null,
  "assumptions": []
}
```

## Agent behavior philosophy

The AI is not the source of spatial truth. The user provides local knowledge. The map/GPS/BPS provides coordinates and anchors. The AI asks questions, classifies instructions, and compiles the result. The reader expands it for the recipient.
