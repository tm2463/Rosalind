import itertools

letters = input('Input characters: ')
n = input('Input integer: ')
if int(n) >= 11:
    raise Exception('Integer must be <= 10')

print("-- Copy --")

my_list = list(itertools.product(str(letters.upper()), repeat = int(n)))
pairs = [str(x) for x in my_list]

for x in pairs:
    print(x.replace("(", '').replace("'", '').replace(",", '').replace(")", '').replace(' ', ''))

print("-- End --")