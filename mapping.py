#!/usr/bin/env python3
import json, sys
if __name__ == '__main__':
    clust_stats = json.load(open(sys.argv[1])) #clust_stats.json

def convert(tricode):
    ss, ds = 0, 0
    mapped = "other"
    for t in tricode:
        if t in ['T', 'S']:
            ss+=1
        if t == 'D':
            ds+=1
    if ss == 3:
        mapped = "ss"
    elif ds == 3:
        mapped = "ds"
    return mapped

mapped_stats = {}
for motif in clust_stats:
    mapped_motif = []
    for cluster in clust_stats[motif]:
        n_ss = 0
        n_ds = 0
        n_other = 0
        for tricode in cluster:
            m = convert(tricode)
            if m == "ss":
                n_ss += cluster[tricode]
            if m == "ds":
                n_ds += cluster[tricode]
            else:
                n_other += cluster[tricode]
        mapped_motif.append([n_ss, n_ds, n_other])
    mapped_stats[motif] = sorted(mapped_motif, key = lambda x: -sum(x))

if __name__ == '__main__':
    json.dump(mapped_stats, open(sys.argv[2], 'w'), indent=2, sort_keys = True)
else:
    result = mapped_stats
#result = {"a":"kakapo"}
