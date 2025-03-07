f = open("rosalind_ba3c.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]

DNA_seq = []
for seq in data:
    DNA_seq.append(seq)

adjacent_list = []
for node in DNA_seq:
    prefix = node[:-1]
    for node_2 in DNA_seq:
        if prefix == node_2[1:]:
            adjacent_list.append([node_2, node])

w = open("output_ba3c.txt", 'w')
for edge in adjacent_list:
    w.write(edge[0]+" -> "+edge[1]+"\n")
w.close()

