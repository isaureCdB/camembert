#!/usr/bin/env python3

'''
./struct-per-fragment.py fragments_clust-aa_missing.json \
    chainsmodels_frag.json clust2Aaa clust2Aaa.json
'''

import json, sys
if __name__ == '__main__':
    fclustaa = json.load(open(sys.argv[1])) #fragments_clust-aa_missing.json
    chains = json.load(open(sys.argv[2])) #chainsmodels_frag.json
    clustkey = sys.argv[3]
else:
    fclustaa = json.loads(fragments)
    chains = json.loads(chainsmodels)

#s = ["G", "U"]
#if na == 'dna':
s = ["G", "T"]

mut = {'G': 'G',
     'A': 'G',
     'C': 'U',
     'U': 'U',
     'T': 'U',
         }

cluster2 = {}
for k in fclustaa:  #k = sequence
    cluster2a = {}
    for kk, frag in fclustaa[k].items():
        try:
            c = frag[clustkey]
        except:
            print(frag, kk)
            raise
        if c not in cluster2a:
            cluster2a[c] = []
        cluster2a[c].append(frag)
    cluster2[k] = cluster2a


cluster2_stats = {}
for motif in cluster2:
    print(motif)
    cluster2_stats[motif] = []
    for clust2a in cluster2[motif].values():
        s2D = {}
        for f in clust2a:
            struc, c, missing =  f['structure'], f['chain'], f['missing_atoms']
            ind = f['indices']
            s2dtot = chains[struc]['ss'][c]
            if sum([int(i )for i in missing]) > 0:
                continue
            s2d = "".join([s2dtot[str(i)][0] for i in ind])
            if s2d not in s2D:
                s2D[s2d] = 0
            s2D[s2d] += 1
        if len(s2D):
            cluster2_stats[motif].append(s2D)

if __name__ == '__main__':
    json.dump(cluster2_stats, open(sys.argv[4], 'w'), indent=2, sort_keys=True)
else:
    result = cluster2_stats
