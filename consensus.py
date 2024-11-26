import os
import re

with open(os.path.expanduser('~/Desktop/rosalind_cons.txt')) as f:
    file = f.read().replace('\n', '')
    file = re.split(r'>Rosalind_.{4}', file)[1:]

length = int(len(file[0]))


def count():
    my_dict = {'A': [0] * length,
               'C': [0] * length,
               'G': [0] * length,
               'T': [0] * length}

    for position in range(0, length):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        for seq in range(0, int(len(file))):
            if file[seq][position] == 'A':
                a_count += 1
            elif file[seq][position] == 'C':
                c_count += 1
            elif file[seq][position] == 'G':
                g_count += 1
            else:
                t_count += 1
            my_dict['A'][position] = a_count
            my_dict['C'][position] = c_count
            my_dict['G'][position] = g_count
            my_dict['T'][position] = t_count

    return my_dict


matrix, consensus_index = count(), []
for x in range(0, length):
    ACGT = []
    for letter in ('A', 'C', 'G', 'T'):
        ACGT.append(matrix[letter][x])
    consensus_index.append(ACGT.index(max(ACGT)))


con_dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
print(''.join(con_dict[x] for x in consensus_index))


for letter, x in zip(['A:', 'C:', 'G:', 'T:'], count().values()):
    print(letter, str(x).replace('[', '').replace(']', '').replace(',', ''))

