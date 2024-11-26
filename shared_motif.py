import os

with open((os.path.expanduser('~/Desktop/rosalind_lcsm.txt')), 'r') as f:
    file = f.read().replace('\n', '').split('>')[1:]
    sequences = [x[13:] for x in file]


def get_kmers(seq, length):
    return [seq[i:i+length] for i in range(len(seq) - length + 1)]


def get_substring(seq_1, seq_2):
    for n in range(1000, 1, -1):
        for x in get_kmers(seq_1, n):
            if x in seq_2:
                return x


substring = get_substring(sequences[0], sequences[1])
for x in range(2, len(sequences)):
    if substring in sequences[x]:
        continue
    else:
        substring = get_substring(sequences[0], sequences[x])

print(substring)
