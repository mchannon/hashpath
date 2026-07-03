#!/usr/bin/env python3
from pathlib import Path
import sys

src = Path("index.hashpath-starter.html")
dst = Path("index.html")
backup = Path("index.before-hashpath-v6.bak.html")

if not src.exists():
    print("ERROR: index.hashpath-starter.html not found. Copy it to the repo root first.", file=sys.stderr)
    sys.exit(1)

if dst.exists() and not backup.exists():
    backup.write_text(dst.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Backed up existing index.html to {backup}")

dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
print("Installed Hashpath v6 as index.html.")
