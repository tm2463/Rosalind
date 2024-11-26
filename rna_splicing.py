from Bio.Seq import Seq
import os

with open(os.path.expanduser('~/Desktop/rosalind_splc.txt')) as f:
    content = f.read().replace('\n', '').split('>')

seq = content[1][13:]
introns = [x[13:] for x in content[2:]]

for intron in introns:
    seq = seq.replace(intron, '')

print(Seq(seq).translate()[:-1])
