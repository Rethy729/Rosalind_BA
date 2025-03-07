f = open("rosalind_ba2c.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

base_index = {'A':0, 'C':1, 'G':2, 'T':3}

sequence = data[0]
k = int(data[1])
profile_matrix = []
for i in range(2, len(data)-1):
    profile_matrix.append(list(map(float, data[i].split(' '))))

probability = []
for i in range(len(sequence)-k+1):
    sub_sequence = sequence[i:i+k]

    prob = 1
    for j in range(len(sub_sequence)):
        prob = prob * profile_matrix[base_index[sub_sequence[j]]][j]
        
    probability.append(prob)

max_prob = max(probability)
print (sequence[probability.index(max_prob):probability.index(max_prob)+k])
