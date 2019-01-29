#!/usr/bin/env python3
import json
fclustaa = json.load(open("./fragments_clust-aa.json"))
chains = json.load(open('chainsmodels_frag.json'))

#fclustaa = json.loads(fragments)
#chains = json.loads(chainsmodels)

js = {}
for motif in fclustaa:
    print(motif)
    js[motif] = fclustaa[motif]
    for k, f in js[motif].items():
        struc, c, resid =  f['structure'], f['chain'], f['resid']
        missing = chains[struc]['missing_atoms'][c]
        miss = []
        for r in resid:
            if r in missing.keys():
                miss.append(int(missing[r]))
            else:
                miss.append(0)
        f['missing_atoms'] = miss

json.dump(js, open('fragments_clust-aa_missing.json', 'w'), indent=2, sort_keys=True)
