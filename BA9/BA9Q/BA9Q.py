from collections import defaultdict
from collections import deque

f = open('rosalind_ba9q.txt', 'r')
data = f.readlines()

text = data[0].strip()
k = int(data[1].strip())

def sort_key_1(string):
    return string.replace('$', ' ')

def sort_key_2(tuple):
    return tuple[0].replace('$', ' ')

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
#print(bwt)

def sort_BWT(bwt):
    bwt_index = []
    index_dict = defaultdict(int)
    for letter in bwt:
        index_dict[letter] += 1
        bwt_index.append((letter, index_dict[letter]))
    sort_bwt_index = sorted(bwt_index, key = sort_key_2)
    return bwt_index, sort_bwt_index

bwt_index, sort_bwt_index = sort_BWT(bwt)

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
answer_lst = []
for i, suffix_num in enumerate(suffix_arr):
    if suffix_num % k == 0:
        answer_lst.append([i, suffix_num])
answer_lst.sort()

for line in answer_lst:
    print(str(line[0])+','+str(line[1]))