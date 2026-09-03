from lingpy import *

seqs = ['Nāman','Nām','Nāv','Nām']

msa = Multiple(seqs)

msa.prog_align()

print(msa)

