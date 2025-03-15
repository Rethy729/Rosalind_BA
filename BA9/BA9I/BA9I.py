from collections import deque
f = open('rosalind_ba9i.txt', 'r')
data = f.readlines()
text = data[0].strip()

def sort_key(string):
    return string.replace('$', ' ')
def BWT(text):

    bwt_lst = []
    text_deque = deque(text)
    for i in range(len(text)):
        bwt_lst.append(str(text_deque))
        text_deque.rotate(1)
    sorted_bwt_lst = sorted(bwt_lst, key = sort_key)
    print (sorted_bwt_lst)
    bwt = []
    for line in sorted_bwt_lst:
        bwt.append(line[-4])
    return bwt
print(''.join(map(str, BWT(text))))
