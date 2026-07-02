#!/usr/bin/env python3
from pathlib import Path
import re
import sys

readme = Path("README.md")
backup = Path("README.before-hashpath-menu.bak.md")
MENU = '<!-- HASHPATH_MENU_BEGIN -->\n\n# Hashpath\n\n**Compact procedural geography for real-world arrivals.**\n\nHashpath is an app, documentation site, and open format for sharing the instructions that ordinary maps do not carry well: parking, gates, doors, access codes, dropoff points, stairs, entrances, exits, fallback steps, and arrival details.\n\nHashsite and Hashpath are companion apps/products:\n\n| Product | Primary job |\n|---|---|\n| **Hashsite** | Compact place codes: mark, copy, text, print, preview, and reopen real-world points. |\n| **Hashpath** | Compact arrival instructions: sequence the real-world procedure around those points. |\n\nHashsite answers:\n\n```text\nWhere is the point?\n```\n\nHashpath answers:\n\n```text\nHow do I actually get there, enter, park, drop off, pick up, or finish the arrival?\n```\n\n## Start here\n\n| Topic | Page |\n|---|---|\n| 1. Why Hashpath? | [`docs/01-WHY-HASHPATH.md`](docs/01-WHY-HASHPATH.md) |\n| 2. What a Hashpath is | [`docs/02-WHAT-IS-A-HASHPATH.md`](docs/02-WHAT-IS-A-HASHPATH.md) |\n| 3. Format and segments | [`docs/03-FORMAT-AND-SEGMENTS.md`](docs/03-FORMAT-AND-SEGMENTS.md) |\n| 4. Places, steps, and labels | [`docs/04-PLACES-STEPS-LABELS.md`](docs/04-PLACES-STEPS-LABELS.md) |\n| 5. Gates, codes, doors, and access | [`docs/05-ACCESS-AND-ARRIVAL.md`](docs/05-ACCESS-AND-ARRIVAL.md) |\n| 6. Examples | [`docs/06-EXAMPLES.md`](docs/06-EXAMPLES.md) |\n| 7. App behavior | [`docs/07-APP-BEHAVIOR.md`](docs/07-APP-BEHAVIOR.md) |\n| 8. AI agents and structured instructions | [`docs/08-AI-AGENTS.md`](docs/08-AI-AGENTS.md) |\n| 9. BPS and local truth anchors | [`docs/09-BPS.md`](docs/09-BPS.md) |\n| 10. Hosted layer and publishing | [`docs/10-HOSTED-LAYER.md`](docs/10-HOSTED-LAYER.md) |\n| 11. Relationship to Hashsite | [`docs/11-HASHSITE-RELATIONSHIP.md`](docs/11-HASHSITE-RELATIONSHIP.md) |\n| 12. Roadmap and design principles | [`docs/12-ROADMAP-DESIGN.md`](docs/12-ROADMAP-DESIGN.md) |\n\n## One-minute version\n\nGetting directions is solved.\n\nGiving directions still sucks.\n\nA map can route you to a street address, pin, or coordinate. But the useful human instruction is often something like:\n\n```text\nUse the west gate.\nEnter code 4729.\nPark behind Building C.\nUse the stairs by the loading dock.\nDoor is on the second level.\nDo not use the main entrance after 6 p.m.\n```\n\nHashpath turns that kind of real-world arrival procedure into a compact, structured, shareable object.\n\n## Live app / site\n\n<https://hashpath.org>\n\n## Companion product\n\nHashsite is the companion app/product for compact place codes.\n\n<https://hashsite.org>\n\n<!-- HASHPATH_MENU_END -->\n'

if not readme.exists():
    print("ERROR: README.md not found. Run from the Hashpath repo root.", file=sys.stderr)
    sys.exit(1)

old = readme.read_text(encoding="utf-8")

if not backup.exists():
    backup.write_text(old, encoding="utf-8")
    print(f"Backed up existing README.md to {backup}")

pattern = re.compile(r"<!-- HASHPATH_MENU_BEGIN -->.*?<!-- HASHPATH_MENU_END -->\n?", re.S)
if pattern.search(old):
    new = pattern.sub(MENU.rstrip() + "\n\n", old)
    print("Replaced existing managed Hashpath menu block.")
else:
    new = MENU.rstrip() + "\n\n" + old
    print("Prepended managed Hashpath menu block and preserved existing README body.")

readme.write_text(new, encoding="utf-8")
