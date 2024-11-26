import os
from Bio.Seq import Seq

with open((os.path.expanduser('~/Desktop/rosalind_prot.txt')), 'r') as f:
    file = f.read().replace('\n', '')

RNA = Seq(file)
print(RNA.translate()[:-1]) # remove asterix marking end codon
