#!/usr/bin/env python3
"""
hashpath_lint.py - draft helper for Hashpath examples.
Usage: python scripts/hashpath_lint.py "#7B0055jFERR>rDWgZAQc4729#p93Ld88K"
"""
from __future__ import annotations
import re, sys
from dataclasses import dataclass
DIRECTIVES={"a":"area/opposite-corner completer","b":"callbox/intercom","c":"payload/code/detail","d":"door/destination/dropoff","e":"entrance/elevator/escalator","g":"gate/guardpost","h":"hazard","i":"information/check-in/reception","j":"deceptive junction/wrong turn","k":"key/keybox/cache","l":"lobby/loading/lounge","m":"meet/pickup/handoff","n":"no-go/avoid area","p":"parking","q":"callpoint/checkpoint","r":"road/route condition","s":"stairs/search sector","t":"tare point/trailhead/transfer","u":"turnaround/U-turn","v":"visual/recognition cue","w":"washroom/water/support","x":"exit","z":"usable zone/general zone"}
OPERATORS={">":"directed/one-way movement operator"}
ANCHOR_RE=re.compile(r"^#([A-Za-z0-9]+)")
@dataclass
class Token:
    kind:str; value:str; meaning:str=""
def lint(hashpath:str)->list[Token]:
    tokens=[]; m=ANCHOR_RE.match(hashpath)
    if not m: raise ValueError("Hashpath must begin with a #FULLCODE anchor.")
    tokens.append(Token("anchor","#"+m.group(1),"full starting Hashsite anchor")); i=m.end()
    while i<len(hashpath):
        ch=hashpath[i]
        if ch in DIRECTIVES:
            meaning=DIRECTIVES[ch]; j=i+1
            while j<len(hashpath) and hashpath[j] not in DIRECTIVES and hashpath[j] not in OPERATORS: j+=1
            val=hashpath[i+1:j]
            tokens.append(Token("directive",ch,meaning))
            tokens.append(Token("payload" if ch=="c" else "suffix",val,"payload following c" if ch=="c" else "spatial suffix or descriptor payload"))
            i=j; continue
        if ch in OPERATORS:
            tokens.append(Token("operator",ch,OPERATORS[ch])); i+=1; continue
        tokens.append(Token("unknown",ch,"unknown character outside directive payload")); i+=1
    return tokens
def main(argv):
    if len(argv)!=2:
        print(__doc__.strip()); return 2
    try: tokens=lint(argv[1].strip())
    except ValueError as e:
        print(f"ERROR: {e}"); return 1
    for t in tokens: print(f"{t.kind:10} {t.value:20} {t.meaning}")
    return 1 if any(t.kind=="unknown" for t in tokens) else 0
if __name__=="__main__": raise SystemExit(main(sys.argv))
