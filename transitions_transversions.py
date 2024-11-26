import os

with open((os.path.expanduser('~/Desktop/rosalind_tran.txt')), 'r') as f:
    file = f.read().replace('\n', '').split('>')[1:]

s1 = file[0][13:]
s2 = file[1][13:]

transitions = 0
transversions = 0

ts_pairs = {('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')}

for x, y in zip(s1, s2):
    if x != y:
        if (x, y) in ts_pairs:
            transitions += 1
        else:
            transversions += 1

print(transitions/transversions)
