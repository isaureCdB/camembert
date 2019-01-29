import numpy as np

def normalize(d):
    motifs = d.keys()
    numpies = {}
    for m in motifs:
        n = np.array(d[m])
        nsum = np.sum(n, axis=0)
        nnorm = n/nsum
        numpies[m] = nnorm
        numpies[m] = numpies[m].flatten() ###seamless bug
    return numpies

def pure(d):
    motifs = d.keys()
    single = {}
    for m in motifs:
        n = np.array(d[m])
        print(n.shape)
        single_ss = np.sum(n[:,1]+n[:,2] <= 0)
        single_ds = np.sum(n[:,0]+n[:,2] <= 0)
        single_other = np.sum(n[:,0]+n[:,1] <= 0)
        single[m] = [int(single_ss), int(single_ds), int(single_other)]
    return single

def singletons(d):
    motifs = d.keys()
    single = {}
    for m in motifs:
        n = np.array(d[m])
        print(n.shape)
        singletons = n[n.sum(axis=1) == 1 ]
        single_ss = np.sum(singletons[:,0] == 1)
        single_ds = np.sum(singletons[:,1] == 1)
        single_other = np.sum(singletons[:,2] == 1)
        single[m] = [int(single_ss), int(single_ds), int(single_other)]
    return single

result = singletons(mapped_stats)
