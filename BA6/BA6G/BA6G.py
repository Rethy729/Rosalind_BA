f = open('rosalind_ba6g.txt', 'r')
data = f.readlines()
permutation = list(map(int, data[0][1:-2].split(' ')))

def lsttostr(lst):
    lst_str = []
    for num in lst:
        if num > 0:
            lst_str.append('+'+str(num))
        else:
            lst_str.append(str(num))
    print('(' + ' '.join(map(str, lst_str)) + ')')

def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(1, len(cycle)//2+1):
        if cycle[2*i-2] < cycle[2*i-1]:
            chromosome.append(cycle[2*i-1]//2)
        else:
            chromosome.append(-cycle[2*i-2]//2)
    (lsttostr(chromosome))

cycle_to_chromosome(permutation)


