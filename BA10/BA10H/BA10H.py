f = open('rosalind_ba10h.txt', 'r')
data = f.readlines()

def data_processing(data):
    string = data[0].strip()
    path = data[4].strip()
    occur = list(map(str, data[2].strip().split()))
    sym = list(map(str, data[6].strip().split()))
    return string, path, occur, sym

string, path, occur, sym = data_processing(data)
print (string, path, occur, sym)

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

e_matrix = emission_matrix(string, path, occur, sym)

def transition_matrix(path, sym):
    t_matrix = []
    for i in range(len(sym)):
        t_matrix.append([0]*len(sym))
    print (t_matrix)
    for i in range(len(path)-1):
        sub_string = path[i:i+2]
        t_matrix[sym.index(sub_string[0])][sym.index(sub_string[1])] += 1
    print (t_matrix)
    for i in range(len(t_matrix)):
        sum_t = sum(t_matrix[i])
        if sum_t == 0:
            for j in range(len(t_matrix[i])):
                t_matrix[i][j] = (1/len(sym))
        else:
            for j in range(len(t_matrix[i])):
                t_matrix[i][j] = t_matrix[i][j] / sum_t
    return t_matrix

t_matrix = transition_matrix(path, sym)

w = open('output_ba10h.txt', 'w')
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