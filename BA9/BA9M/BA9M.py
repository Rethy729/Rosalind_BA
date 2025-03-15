from collections import defaultdict

f = open('rosalind_ba9m.txt', 'r')
data = f.readlines()

def data_processing(data):
    text = data[0].strip()
    patterns = list(map(str, data[1].strip().split(' ')))
    return text, patterns

text, patterns = data_processing(data)
#print (text)
#print (patterns)

def sort_key(tuple):
    return tuple[0].replace('$', ' ')

def sort_BWT(bwt):
    bwt_index = []
    index_dict = defaultdict(int)
    for letter in bwt:
        index_dict[letter] += 1
        bwt_index.append((letter, index_dict[letter]))
    sort_bwt_index = sorted(bwt_index, key=sort_key)
    return bwt_index, sort_bwt_index

bwt_index, sort_bwt_index = sort_BWT(text)
#print (bwt_index)
#print (sort_bwt_index)

def first_occurrance(sort_bwt_index):
    occurrance = [0, 0, 0, 0]
    for i, tuple in enumerate(sort_bwt_index):
        if tuple[0] == 'A':
            occurrance[0] = i
            break
    for i, tuple in enumerate(sort_bwt_index):
        if tuple[0] == 'C':
            occurrance[1] = i
            break
    for i, tuple in enumerate(sort_bwt_index):
        if tuple[0] == 'G':
            occurrance[2] = i
            break
    for i, tuple in enumerate(sort_bwt_index):
        if tuple[0] == 'T':
            occurrance[3] = i
            break
    return occurrance

first_occurrance_lst = first_occurrance(sort_bwt_index)
#print (first_occurrance_lst)

def count(bwt_index):
    count = []
    for i in range(4):
        count.append([0]*(len(bwt_index)+1))
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i, tuple in enumerate(bwt_index):
        if tuple[0] == 'A':
            count_a += 1
        elif tuple[0] == 'C':
            count_c += 1
        elif tuple[0] == 'G':
            count_g += 1
        elif tuple[0] == 'T':
            count_t += 1
        count[0][i+1] = count_a
        count[1][i+1] = count_c
        count[2][i+1] = count_g
        count[3][i+1] = count_t
    return count

count = count(bwt_index)
#print(count)
def last_to_first(bwt_index, sort_bwt_index, idx):
    tuple = bwt_index[idx]
    return sort_bwt_index.index(tuple)

#print (last_to_first(bwt_index, sort_bwt_index, 4))

def BWM_matching(text, bwt_index, pattern):
    top = 0
    bottom = len(bwt_index)-1
    symbol_lex = {'A':0, 'C':1, 'G':2, 'T':3}
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in text[top:bottom+1]:
                top = first_occurrance_lst[symbol_lex[symbol]] + count[symbol_lex[symbol]][top]
                bottom = first_occurrance_lst[symbol_lex[symbol]] + count[symbol_lex[symbol]][bottom+1] - 1
            else:
                return 0
        else:
            return bottom - top + 1

for pattern in patterns:
    print (BWM_matching(text, bwt_index, pattern), end = ' ')
