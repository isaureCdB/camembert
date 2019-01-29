#!/usr/bin/env python3
import json, sys
js = json.load(open(sys.argv[1]))

new = {}
for k in js:
    kk = sorted(js[k].keys())[:10]
    new[k] = {}
    for i in kk:
        new[k][i] = js[k][i]

json.dump(new, open(sys.argv[2], 'w'), indent=2, sort_keys=True)
