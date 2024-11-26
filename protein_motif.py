import requests
import os
import re

with open((os.path.expanduser('~/Desktop/rosalind_mprt.txt')), 'r') as f:
    uniprot = [x.rstrip('\n') for x in f]
    sequences = [requests.get('https://rest.uniprot.org/uniprotkb/' + x[:6] + '.fasta').text.split('\n') for x in uniprot]

#parse FASTA files
my_dict = {}
label = None
for fasta in sequences:
    for line in fasta:
        if line.startswith('>'):
            label = line[4:10]
            my_dict[label] = ''
        else:
            my_dict[label] += line

for x, y in zip(my_dict, uniprot):
    locations = list(re.finditer(r'(?=(N[^P][ST][^P]))', my_dict[x]))
    if locations:
        print(y)
        print(str([location.start() + 1 for location in locations]).replace('[', '').replace(']', '').replace(',',''))
