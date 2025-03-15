from collections import defaultdict

f = open('rosalind_ba9j.txt', 'r')
data = f.readlines()
BWT = data[0].strip()

def sort_key(tuple):
    return tuple[0].replace('$', ' ')

def inverse_BWT(bwt):
    bwt_with_index = []
    index_dict = defaultdict(int)
    for letter in bwt:
        index_dict[letter] += 1
        bwt_with_index.append((letter, index_dict[letter]))

    bwt_sort = sorted(bwt_with_index, key = sort_key)
    print(bwt_sort)
    print (bwt_with_index)

    reconstruct = ''
    index = 0
    while bwt_with_index[index][0] != '$':
        reconstruct = bwt_with_index[index][0] + reconstruct
        index = bwt_sort.index(bwt_with_index[index])
    return (reconstruct + '$')

print (inverse_BWT(BWT))
