from Bio.Seq import Seq
import os

with open((os.path.expanduser('~/Desktop/rosalind_orf.txt')), 'r') as f:
    file = f.read().split('\n')[1:]
    seq = Seq(''.join(x for x in file))
    rev_seq = seq.reverse_complement()

for x in range(len(seq)):
    if seq[x:x+3] == 'ATG':
        orf = seq[x:]
        if '*' in orf.translate():
            print(orf.translate(to_stop= True))
    elif rev_seq[x:x+3] == 'ATG':
        orf = rev_seq[x:]
        if '*' in orf.translate():
            print(orf.translate(to_stop= True))
