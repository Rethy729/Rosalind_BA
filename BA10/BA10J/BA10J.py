f = open('rosalind_ba10j.txt', 'r')
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
    return string, occur, sym, trans_matrix, ems_matrix

string, occur, sym, trans_matrix, ems_matrix = data_processing (data)

def weight_matrix_build(sym, occur, trans_matrix, ems_matrix):
    weight_matrix = []
    for i in range(len(sym) * len(sym)):
        weight_matrix.append([0] * len(occur))
    for i in range(len(sym)):
        for j in range(len(sym)):
            for k in range(len(occur)):
                weight_matrix[i * len(sym) + j][k] = trans_matrix[j][i] * ems_matrix[i][k]  # 열 순서 -> A->A, B->A, C->A ... last->A, A->B, B->B, C->B, ... last -> B, ... // 행 순서: x, y, z ...
    return weight_matrix

weight_matrix= weight_matrix_build(sym, occur, trans_matrix, ems_matrix)

def forward_back(string, occur, sym, trans_matrix, ems_matrix):

    print (string)
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

    print (viterbi)
    prob_sum = 0    #we get forward(sink)
    for i in range(len(sym)):
        prob_sum += viterbi[i][-1]

    string_rev = string[::-1]
    print (string_rev)

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
    print (viterbi_rev)
    return viterbi, viterbi_rev, prob_sum

viterbi, viterbi_rev, prob_sum = forward_back(string, occur, sym, trans_matrix, ems_matrix)

def p_profile(viterbi, viterbi_rev, prob_sum, string, sym):
    p_profile = []
    for i in range(len(string)):
        occur_profile = []
        for j in range(len(sym)):
            occur_profile.append(viterbi[j][i]*viterbi_rev[j][len(string)-i-1]/prob_sum)
        sum_p = sum(occur_profile)
        for j in range(len(sym)):
            occur_profile[j] = occur_profile[j] / sum_p
        p_profile.append(occur_profile)
    return (p_profile)

answer = p_profile(viterbi, viterbi_rev, prob_sum, string, sym)

w = open('output_ba10j.txt', 'w')
w.write(' '.join(map(str, sym))+'\n')
for i in range(len(answer)):
    w.write(' '.join(map(str, answer[i]))+'\n')
w.close()