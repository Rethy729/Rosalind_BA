f = open('rosalind_ba6a.txt', 'r')
data = f.readlines()
permutation = list(map(int, data[0][1:-1].split(' ')))

def lsttostr(lst):
    lst_str = []
    for num in lst:
        if num > 0:
            lst_str.append('+'+str(num))
        else:
            lst_str.append(str(num))
    print('(' + ' '.join(map(str, lst_str)) + ')')

def reversal(lst, start, end): #1_based
    lst_rev = []
    for i in range(end-1, start-2, -1):
        lst_rev.append(-lst[i])
    for i in range(start-1, end):
        lst[i] = lst_rev[i-(start-1)]

def GreedySorting(lst):
    for i in range(1, len(lst)+1):
        if lst[i-1] != i:
            if i in lst:
                endpoint = lst.index(i)
                reversal(lst, i, endpoint+1)
                lsttostr(permutation)

            elif -i in lst:
                endpoint = lst.index(-i)
                reversal(lst, i, endpoint + 1)
                lsttostr(permutation)
        else:
            continue

        if lst[i-1] == -i:
            reversal(lst, i, i)
            lsttostr(permutation)

GreedySorting(permutation)
