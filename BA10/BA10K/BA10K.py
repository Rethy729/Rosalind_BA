f = open('rosalind_ba10k.txt', 'r')
data = f.readlines()

def data_processing (data):
    iter = int(data[0])
    string = data[2].strip()
    occur = list(map(str, data[4].split()))
    sym = list(map(str, data[6].split()))
    trans_matrix = []
    ems_matrix = []
    for i in range(9, 9+len(sym)):
        trans_matrix.append(list(map(float, data[i].strip().split()[1:])))  # 열 순서 = 행 순서 = A, B, C, D...
    for i in range(11+len(sym), 11 + 2*len(sym)):
        ems_matrix.append(list(map(float, data[i].strip().split()[1:]))) # 열 순서 = A, B, C, D ... // 행 순서 = x, y, z, ...
    return iter, string, occur, sym, trans_matrix, ems_matrix



def weight_matrix_build(sym, occur, trans_matrix, ems_matrix):
    weight_matrix = []
    for i in range(len(sym) * len(sym)):
        weight_matrix.append([0] * len(occur))
    for i in range(len(sym)):
        for j in range(len(sym)):
            for k in range(len(occur)):
                weight_matrix[i * len(sym) + j][k] = trans_matrix[j][i] * ems_matrix[i][k]  # 열 순서 -> A->A, B->A, C->A ... last->A, A->B, B->B, C->B, ... last -> B, ... // 행 순서: x, y, z ...
    return weight_matrix



def forward_back(string, occur, sym, trans_matrix, ems_matrix):

    #print (string)
    initial_lst = [0]*len(sym) #initial node weight
    initial_occur = string[0]
    for i in range(len(sym)):
        initial_lst[i] = (1/len(sym)) * ems_matrix[i][occur.index(initial_occur)]

    viterbi = [] #viterbi = len(sym) as num of row, len(string) as num of column
    for i in range(len(sym)):
        viterbi.append([0]*len(string))
    for i in range(len(sym)):
        viterbi[i][0] = initial_lst[i]

    for i in range(1, len(string)):  #build viterbi matrix
        for j in range(len(sym)):
            cand = []
            for k in range(j*len(sym), (j+1)*len(sym)):
                cand.append(viterbi[k-j*len(sym)][i-1] * weight_matrix[k][occur.index(string[i])])
            viterbi[j][i] = sum(cand)

    prob_sum = 0    #we get forward(sink)
    for i in range(len(sym)):
        prob_sum += viterbi[i][-1]

    string_rev = string[::-1]

    viterbi_rev = []  # viterbi = len(sym) as num of row, len(string) as num of column
    for i in range(len(sym)):
        viterbi_rev.append([0] * len(string))
    for i in range(len(sym)):
        viterbi_rev[i][0] = 1

    for i in range(1, len(string)):  # build viterbi matrix reverse
        for j in range(len(sym)):
            cand = []
            for k in range(j, (len(sym)**2), len(sym)):
                    cand.append(viterbi_rev[(k-j)//len(sym)][i - 1] * weight_matrix[k][occur.index(string_rev[i-1])])
            viterbi_rev[j][i] = sum(cand)

    return viterbi, viterbi_rev, prob_sum



def e_profile_build(viterbi, viterbi_rev, prob_sum, string, sym):
    e_profile = []
    for i in range(len(string)):
        occur_profile = []
        for j in range(len(sym)):
            occur_profile.append(viterbi[j][i]*viterbi_rev[j][len(string)-i-1]/prob_sum)
        sum_p = sum(occur_profile)
        for j in range(len(sym)):
            occur_profile[j] = occur_profile[j] / sum_p
        e_profile.append(occur_profile)
    return (e_profile)



def t_profile_build (viterbi, viterbi_rev, prob_sum, string, sym, occur):
    t_profile = []
    for i in range(len(string)-1): #행: len(string)-1 // 열: AA, AB, AC, BA, BB, BC .....
        t_profile_temp =[]
        for j in range(len(sym)):
            for k in range(len(sym)):
                t_profile_temp.append(viterbi[j][i] * viterbi_rev[k][len(string)-2-i] * weight_matrix[j+len(sym)*k][occur.index(string[i+1])])
        t_profile.append(t_profile_temp)
    return (t_profile)



def build_t_matrix(t_profile, sym):
    t_matrix = []
    for i in range(len(sym)):
        sum_lst = [0]*len(sym)
        for k in range(len(t_profile)):
            for j in range(i*len(sym), (i+1)*len(sym)):
                sum_lst[j-i*len(sym)] += t_profile[k][j]

        sum_sym = sum(sum_lst)
        for j in range(len(sym)):
            sum_lst[j] = sum_lst[j]/sum_sym
        t_matrix.append(sum_lst)
    return t_matrix

def build_e_matrix(string, e_profile, sym, occur):
    e_matrix = []
    for i in range(len(sym)):
        e_matrix.append([0]*len(occur))

    for i in range(len(string)):
        for j in range(len(sym)):
            e_matrix[j][occur.index(string[i])] += e_profile[i][j]

    for row in e_matrix:
        sum_row = sum(row)
        for i in range(len(row)):
            row[i] = row[i]/sum_row
    return e_matrix

iter, string, occur, sym, trans_matrix_i, ems_matrix_i = data_processing(data)
weight_matrix= weight_matrix_build(sym, occur, trans_matrix_i, ems_matrix_i)
viterbi, viterbi_rev, prob_sum = forward_back(string, occur, sym, trans_matrix_i, ems_matrix_i)
e_profile = e_profile_build(viterbi, viterbi_rev, prob_sum, string, sym)
t_profile = t_profile_build(viterbi, viterbi_rev, prob_sum, string, sym, occur)
t_matrix = build_t_matrix(t_profile, sym)
e_matrix = build_e_matrix(string, e_profile, sym, occur)

for i in range(iter-1):
    weight_matrix = weight_matrix_build(sym, occur, t_matrix, e_matrix)
    viterbi, viterbi_rev, prob_sum = forward_back(string, occur, sym, t_matrix, e_matrix)
    e_profile = e_profile_build(viterbi, viterbi_rev, prob_sum, string, sym)
    t_profile = t_profile_build(viterbi, viterbi_rev, prob_sum, string, sym, occur)
    t_matrix = build_t_matrix(t_profile, sym)
    e_matrix = build_e_matrix(string, e_profile, sym, occur)

print (t_matrix)
print (e_matrix)

w = open('output_ba10k.txt', 'w')
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