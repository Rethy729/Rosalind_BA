from collections import defaultdict

f = open('rosalind_ba9l.txt', 'r')
data = f.readlines()

def data_processing(data):
    text = data[0].strip()
    patterns = list(map(str, data[1].strip().split(' ')))
    return text, patterns

text, patterns = data_processing(data)
print (text)
print (patterns)

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
print (bwt_index)
print (sort_bwt_index)

def last_to_first(bwt_index, sort_bwt_index, idx):
    tuple = bwt_index[idx]
    return sort_bwt_index.index(tuple)

#print (last_to_first(bwt_index, sort_bwt_index, 4))

def BWM_matching(text, bwt_index, sort_bwt_index, pattern):
    top = 0
    bottom = len(bwt_index)-1

    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]

            btw_index_cut = bwt_index[top:bottom + 1]
            if symbol in text[top:bottom+1]:
                for i, tuple in enumerate(btw_index_cut):
                    if tuple[0] == symbol:
                        t_index = i + top
                        break

                btw_index_cut.reverse()
                for j, tuple in enumerate(btw_index_cut):
                    if tuple[0] == symbol:
                        b_index = bottom - j
                        break
                top = last_to_first(bwt_index, sort_bwt_index, t_index)
                bottom = last_to_first(bwt_index, sort_bwt_index, b_index)
            else:
                return 0
        else:
            return bottom - top + 1

for pattern in patterns:
    print (BWM_matching(text, bwt_index, sort_bwt_index, pattern), end = ' ')
