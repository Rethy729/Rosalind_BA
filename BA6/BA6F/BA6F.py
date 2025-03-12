f = open('rosalind_ba6f.txt', 'r')
data = f.readlines()
permutation = list(map(int, data[0][1:-2].split(' ')))

def chromosome_to_cycle(lst):
    cycle = []
    for i in lst:
        if i > 0:
            cycle.append(2*i-1)
            cycle.append(2*i)
        else:
            cycle.append(2*-i)
            cycle.append(2*-i-1)

    return cycle

print ('('+ ' '.join(map(str, chromosome_to_cycle(permutation))) + ')')
