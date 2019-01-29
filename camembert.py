import json
from seamless.highlevel import Context

ctx = Context()
#ctx.fragments = json.load(open("fragments_clust-aa.json"))
#ctx.fragments.celltype = "json"
ctx.fragments = ""
ctx.fragments.celltype = "text"
#ctx.chainsmodels = json.load(open("chainsmodels_frag.json"))
#ctx.chainsmodels.celltype = "json"
ctx.chainsmodels = ""
ctx.chainsmodels.celltype = "text"
ctx.struct_per_fragment = lambda fragments, chainsmodels, na, clustkey: None
ctx.struct_per_fragment.fragments = ctx.fragments
ctx.struct_per_fragment.chainsmodels = ctx.chainsmodels
ctx.struct_per_fragment.na = "rna"
ctx.struct_per_fragment.clustkey = "clust1Aaa"
ctx.code >> ctx.struct_per_fragment.code
ctx.clust_stats = ctx.struct_per_fragment
ctx.clust_stats.celltype = "json"
ctx.clust_stats.mount("clust-stats.json")


ctx.mapping = lambda clust_stats: None
ctx.mapping.clust_stats = ctx.clust_stats
ctx.code_mapping >> ctx.mapping.code
ctx.mapped_stats = ctx.mapping
ctx.mapped_stats.celltype = "json"
ctx.mapped_stats.mount("mapped-stats.json")

ctx.norm_stats = lambda mapped_stats: None
ctx.norm_stats.mapped_stats = ctx.mapped_stats
ctx.code_norm_stats >> ctx.norm_stats.code

ctx.normed_stats = ctx.norm_stats
ctx.normed_stats.mount("normed-stats", persistent=False)

print("load JSON data...")
ctx.fragments.set(open("fragments_clust-aa_missing.json").read())
ctx.chainsmodels.set(open("chainsmodels_frag.json").read())

print("mount code files...")
ctx.code_norm_stats.mount("norm_stats.py", authority="file")
ctx.code_mapping.mount("mapping.py", authority="file")
ctx.code.mount("struct-per-fragment.py", authority="file")

#ctx.translate(force=True)
ctx.equilibrate()
