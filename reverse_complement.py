from Bio.Seq import Seq
import os

with open((os.path.expanduser('~/Desktop/rosalind_revc.txt')), 'r') as f:
    file = f.read().replace('\n', '')

my_seq = Seq(file)
print(my_seq.reverse_complement())
