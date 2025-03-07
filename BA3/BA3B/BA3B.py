f = open("rosalind_ba3b.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]

DNA_seq = []
for seq in data:
    DNA_seq.append(seq)

spelled = ''
spelled = spelled+DNA_seq[0]

for i in range(1, len(DNA_seq)):
    spelled = spelled + DNA_seq[i][-1]

w = open('output_ba3b.txt', 'w')
w.write(spelled)
w.close()
