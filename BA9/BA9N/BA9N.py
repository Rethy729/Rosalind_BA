from collections import defaultdict
from collections import deque

f = open('rosalind_ba9n.txt', 'r')
data = f.readlines()

def sort_key_1(string):
    return string.replace('$', ' ')

def sort_key_2(tuple):
    return tuple[0].replace('$', ' ')

def data_processing(data):
    text = data[0].strip()
    patterns = []
    for line in data[1:]:
        patterns.append(line.strip())
    return text, patterns

text, patterns = data_processing(data)
text = text+'$'

#print (text)
#print (patterns)

def BWT(text):
    bwt_lst = []
    text_deque = deque(text)
    for i in range(len(text)):
        bwt_lst.append(str(text_deque))
        text_deque.rotate(1)
    sorted_bwt_lst = sorted(bwt_lst, key = sort_key_1)
    bwt = []
    for line in sorted_bwt_lst:
        bwt.append(line[-4])
    return bwt

bwt = ''.join(map(str, BWT(text)))
#print (bwt)

def sort_BWT(bwt):
    bwt_index = []
    index_dict = defaultdict(int)
    for letter in bwt:
        index_dict[letter] += 1
        bwt_index.append((letter, index_dict[letter]))
    sort_bwt_index = sorted(bwt_index, key = sort_key_2)
    return bwt_index, sort_bwt_index

bwt_index, sort_bwt_index = sort_BWT(bwt)
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

def suffix_array(bwt_index, sort_bwt_index):
    suffix_array = [0]*len(text)

    suffix_index = len(text)-1
    symbol = '$'
    rank = 1
    while suffix_index != 0:
        idx = sort_bwt_index.index((symbol, rank))
        suffix_array[idx] = suffix_index
        suffix_index -= 1
        symbol = bwt_index[idx][0]
        rank = bwt_index[idx][1]
    return suffix_array

suffix_arr = suffix_array(bwt_index, sort_bwt_index)

def BWM_matching(bwt, bwt_index, pattern, suffix_array):
    top = 0
    bottom = len(bwt_index)-1
    symbol_lex = {'A':0, 'C':1, 'G':2, 'T':3}
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in bwt[top:bottom+1]:
                top = first_occurrance_lst[symbol_lex[symbol]] + count[symbol_lex[symbol]][top]
                bottom = first_occurrance_lst[symbol_lex[symbol]] + count[symbol_lex[symbol]][bottom+1] - 1
            else:
                return 0
        else:
            return suffix_array[top:bottom+1]

answer = []
for pattern in patterns:
    answer_list = BWM_matching(bwt, bwt_index, pattern, suffix_arr)
    if answer_list != 0:
        answer += answer_list
answer.sort()
print (' '.join(map(str, answer)))