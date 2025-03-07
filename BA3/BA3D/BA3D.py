
f = open("rosalind_ba3d.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
k = int(data[0])
text = data[1]

DeBruijn = {}

for i in range(len(text)-k+1):
    sub_text = text[i:i+k]
    if sub_text[:-1] in DeBruijn:
        DeBruijn[sub_text[:-1]].append(sub_text[1:])
    else:
        DeBruijn[sub_text[:-1]] = [sub_text[1:]]

w = open('output_ba3d.txt', 'w')

for key in DeBruijn:
    w.write(key + ' -> '+','.join(map(str, DeBruijn[key]))+'\n')

w.close()

"""

test = {}
test['AAT'] = ['ATA']
print test
test['AAT'].append('TAT')
print test
"""
