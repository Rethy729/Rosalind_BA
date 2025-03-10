f = open("rosalind_ba3l.txt", 'r')
data = f.readlines()
k = list(map(int, data[0].split(' ')))[0]
d = list(map(int, data[0].split(' ')))[1]
dataline = len(data)-1

def debrujin(data):
    path = []
    for line in data[1:]:
        kdmer_lst = list(map(str, line.strip().split('|')))
        path.append(kdmer_lst)
    return path

def list_to_string(lst):
    sum_prefix_lst = []
    sum_suffix_lst = []

    for i in range(len(lst)-1):
        sum_prefix_lst.append(lst[i][0]+lst[i+1][0][-1])
        sum_suffix_lst.append(lst[i][1]+lst[i+1][1][-1])

    prefix_str = sum_prefix_lst[0]
    suffix_str = sum_suffix_lst[0]

    for string in sum_prefix_lst[1:]:
        prefix_str += string[-1]

    for string in sum_suffix_lst[1:]:
        suffix_str += string[-1]

    match = 2*(k+dataline-1) - ((2*k)+d+dataline-1)
    return prefix_str + suffix_str[match:]

print (list_to_string(debrujin(data)))