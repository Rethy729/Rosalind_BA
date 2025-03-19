f = open('rosalind_ba10d.txt', 'r')
data = f.readlines()

def data_processing (data):
    string = data[0].strip()
    occur = list(map(str, data[2].split()))
    sym = list(map(str, data[4].split()))
    trans_matrix = []
    ems_matrix = []
    for i in range(7, 7+len(sym)):
        trans_matrix.append(list(map(float, data[i].strip().split()[1:])))  # 열 순서 = 행 순서 = A, B, C, D...
    for i in range(9+len(sym), 9 + 2*len(sym)):
        ems_matrix.append(list(map(float, data[i].strip().split()[1:]))) # 열 순서 = A, B, C, D ... // 행 순서 = x, y, z, ...
    weight_matrix = []
    for i in range(len(sym)*len(sym)):
        weight_matrix.append([0]*len(occur))
    for i in range(len(sym)):
        for j in range(len(sym)):
            for k in range(len(occur)):
                weight_matrix[i*len(sym)+j][k] = trans_matrix[j][i] * ems_matrix[i][k] #열 순서 -> A->A, B->A, C->A ... last->A, A->B, B->B, C->B, ... last -> B, ... // 행 순서: x, y, z ...
    return string, occur, sym, trans_matrix, ems_matrix, weight_matrix

#print (data_processing(data))
string, occur, sym, trans_matrix, ems_matrix, weight_matrix = data_processing(data)

def viterbi(string, occur, sym, trans_matrix, ems_matrix, weight_matrix):
    initial_lst = [0]*len(sym)
    initial_occur = string[0]
    for i in range(len(sym)):
        initial_lst[i] = (1/len(sym)) * ems_matrix[i][occur.index(initial_occur)]
    #print (initial_lst)
    viterbi = []
    for i in range(len(sym)):
        viterbi.append([0]*len(string))
    for i in range(len(sym)):
        viterbi[i][0] = initial_lst[i]
    #print (viterbi)

    for i in range(1, len(string)):
        for j in range(len(sym)):
            cand = []
            for k in range(j*len(sym), (j+1)*len(sym)):
                cand.append(viterbi[k-j*len(sym)][i-1] * weight_matrix[k][occur.index(string[i])])
            viterbi[j][i] = sum(cand)

    prob_sum = 0
    for i in range(len(sym)):
        prob_sum += viterbi[i][-1]
    #print (viterbi)
    return prob_sum

prob_sum = viterbi(string, occur, sym, trans_matrix, ems_matrix, weight_matrix)
print (prob_sum)

