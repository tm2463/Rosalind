import itertools

n = 5


def get_numbers(n):
    seq = [x for x in range(-n, n+1)]
    seq.remove(0)
    return seq

def check_absolute(lst):
    seen = []
    for x in list(lst):
        if abs(x) in seen:
            return False
        else:
            seen.append(abs(x))
        if len(seen) == len(lst):
            return True


generator = list(itertools.permutations(get_numbers(n), n))
ans_list = []
for x in generator:
    lt = list(x)
    if check_absolute(lt) == True:
        ans_list.append(str(x).replace('(', '').replace(')', '').replace(',', ''))

print(len(ans_list))
for x in ans_list:
    print(x)
