import re
import os

with open((os.path.expanduser('~/Desktop/rosalind_subs.txt')), 'r') as f:
    file = f.read().split('\n')

seq = file[0]
motif = r'(?=(' + file[1] + '))'
motifs = re.finditer(motif, seq)

for motif in motifs:
    print(motif.start()+1)
