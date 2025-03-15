from collections import defaultdict

f = open('rosalind_ba9k.txt', 'r')
data = f.readlines()
BWT = data[0].strip()
i = int(data[1].strip())

def sort_key(tuple):
    return tuple[0].replace('$', ' ')

def inverse_BWT(bwt):
    bwt_with_index = []
    index_dict = defaultdict(int)
    for letter in bwt:
        index_dict[letter] += 1
        bwt_with_index.append((letter, index_dict[letter]))

    bwt_sort = sorted(bwt_with_index, key = sort_key)
    tuple = bwt_with_index[i]
    return (bwt_sort.index(tuple))

print(inverse_BWT(BWT))
