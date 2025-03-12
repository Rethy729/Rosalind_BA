f = open('rosalind_ba6b.txt', 'r')
data = f.readlines()
permutation = list(map(int, data[0][1:-2].split(' ')))

def num_breakpoint(lst):
    length = len(lst)
    lst_new = [0] + lst + [length+1]

    bp = 0
    for i in range(0, len(lst_new)-1):
        if lst_new[i] + 1 != lst_new[i+1]:
            bp += 1
    print (bp)

num_breakpoint(permutation)