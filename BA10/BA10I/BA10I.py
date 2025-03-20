f = open('rosalind_ba10i.txt', 'r')
data = f.readlines()

def data_processing(data):
    iter = int(data[0])
    string = data[2].strip()
    occur = list(map(str, data[4].split()))
    sym = list(map(str, data[6].split()))

    t_matrix = []
    e_matrix = []
    for i in range(9, 9 + len(sym)):
        t_matrix.append(list(map(float, data[i].strip().split()[1:])))  # 열 순서 = 행 순서 = A, B, C, D...
    for i in range(11 + len(sym), 11 + 2 * len(sym)):
        e_matrix.append(list(map(float, data[i].strip().split()[1:])))  # 열 순서 = A, B, C, D ... // 행 순서 = x, y, z ..
    return iter, string, occur, sym, t_matrix, e_matrix

def weight_matrix_build(sym, occur, trans_matrix, ems_matrix):
    weight_matrix = []
    for i in range(len(sym) * len(sym)):
        weight_matrix.append([0] * len(occur))
    for i in range(len(sym)):
        for j in range(len(sym)):
            for k in range(len(occur)):
                weight_matrix[i * len(sym) + j][k] = trans_matrix[j][i] * ems_matrix[i][k]  # 열 순서 -> A->A, B->A, C->A ... last->A, A->B, B->B, C->B, ... last -> B, ... // 행 순서: x, y, z ...
    return weight_matrix

def viterbi(string, occur, sym, trans_matrix, ems_matrix):

    weight_matrix = weight_matrix_build(sym, occur, trans_matrix, ems_matrix)
    initial_lst = [0]*len(sym)
    initial_occur = string[0]
    for i in range(len(sym)):
        initial_lst[i] = (1/len(sym)) * ems_matrix[i][occur.index(initial_occur)]
    viterbi = []
    index = []
    for i in range(len(sym)):
        viterbi.append([0]*len(string))
        index.append([0] * len(string))
    for i in range(len(sym)):
        viterbi[i][0] = initial_lst[i]
    for i in range(1, len(string)):
        for j in range(len(sym)):
            cand = []
            for k in range(j*len(sym), (j+1)*len(sym)):
                cand.append(viterbi[k-j*len(sym)][i-1] * weight_matrix[k][occur.index(string[i])])
            viterbi[j][i] = max(cand)
            index[j][i] += cand.index(viterbi[j][i])
    return viterbi, index

def path_print (viterbi_graph, index, sym):
    last_row = []
    for i in range(len(viterbi_graph)):
        last_row.append(viterbi_graph[i][-1])
    last_index = last_row.index(max(last_row))
    path = sym[last_index]

    for i in range(len(index[0])-1, 0, -1):
        last_index = index[last_index][i]
        path = sym[last_index] + path

    return path

def emission_matrix(string, path, occur, sym):
    e_matrix = []
    for i in range(len(sym)):
        e_matrix.append([0]*len(occur))
    for i in range(len(path)):
        e_matrix[sym.index(path[i])][occur.index(string[i])] += 1
    for i in range(len(e_matrix)):
        sum_e = sum(e_matrix[i])
        if sum_e == 0:
            for j in range(len(e_matrix[i])):
                e_matrix[i][j] = (1/len(occur))
        else:
            for j in range(len(e_matrix[i])):
                e_matrix[i][j] = e_matrix[i][j] / sum_e
    return e_matrix

def transition_matrix(path, sym):
    t_matrix = []
    for i in range(len(sym)):
        t_matrix.append([0]*len(sym))
    for i in range(len(path)-1):
        sub_string = path[i:i+2]
        t_matrix[sym.index(sub_string[0])][sym.index(sub_string[1])] += 1
    for i in range(len(t_matrix)):
        sum_t = sum(t_matrix[i])
        if sum_t == 0:
            for j in range(len(t_matrix[i])):
                t_matrix[i][j] = (1/len(sym))
        else:
            for j in range(len(t_matrix[i])):
                t_matrix[i][j] = t_matrix[i][j] / sum_t
    return t_matrix

iter, string, occur, sym, t_matrix_i, e_matrix_i = data_processing(data)   #intial data
viterbi_graph, index = viterbi(string, occur, sym, t_matrix_i, e_matrix_i)
path = path_print (viterbi_graph, index, sym)
e_matrix = emission_matrix(string, path, occur, sym)
t_matrix = transition_matrix(path, sym)

for _ in range(iter-1):
    viterbi_graph, index = viterbi(string, occur, sym, t_matrix, e_matrix)
    path = path_print(viterbi_graph, index, sym)
    e_matrix = emission_matrix(string, path, occur, sym)
    t_matrix = transition_matrix(path, sym)

print (e_matrix)
print (t_matrix)

w = open('output_ba10i.txt', 'w')
w.write(' '.join(map(str, sym))+'\n')
for i in range(len(t_matrix)):
    if i == len(t_matrix)-1:
        w.write(sym[i] + ' ' + ' '.join(map(str, t_matrix[i]))+'\n' + '--------')
    else:
        w.write(sym[i]+ ' ' + ' '.join(map(str, t_matrix[i]))+'\n')
w.write('\n')
w.write(' '.join(map(str, occur))+'\n')
for i in range(len(e_matrix)):
    w.write(sym[i] + ' ' + ' '.join(map(str, e_matrix[i]))+'\n')
w.close()