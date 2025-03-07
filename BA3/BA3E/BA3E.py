f = open("rosalind_ba3e.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]

k = len(data[0])
DeBruijn = {}

for i in range(len(data)):
    sub_text = data[i]
    if sub_text[:-1] in DeBruijn:
        DeBruijn[sub_text[:-1]].append(sub_text[1:])
    else:
        DeBruijn[sub_text[:-1]] = [sub_text[1:]]

w = open('output_ba3e.txt', 'w')

for key in DeBruijn:
    w.write(key + ' -> '+','.join(map(str, DeBruijn[key]))+'\n')

w.close()
