f = open('ATGC.txt', 'r')
data = f.readlines()
char_lst = ['A','T','G','C','-']
ATGC = []
for line in data[1:]:
    ATGC.append(list(map(int, line.split())))
#print (ATGC)

f = open('rosalind_ba5h.txt', 'r')
data = f.readlines()
string_1 = (list(map(str, data[0].strip())))
string_2 = (list(map(str, data[1].strip())))

indel = -1 #score of indel

def matrix_maker(str1, str2, score): #str1 is horizontal, str2 is vertical
    diago = []

    for i in range(len(str2)):
        diago_row = []
        char_2 = str2[i]
        char_2_index = char_lst.index(char_2)
        for j in range(len(str1)):
            char_1 = str1[j]
            char_1_index = char_lst.index(char_1)
            diago_row.append(score[char_1_index][char_2_index])
        diago.append(diago_row)

    return diago

def DP(diago):
    n = len(diago[0])+1 #the horizontal length of the matrix
    m = len(diago)+1 #the vertical length of the matrix
    score_matrix = []

    for i in range(m):
        score_matrix.append([-99999999]*n)

    for i in range(n):
        score_matrix[0][i] = 0 #start from some point on first row

    for i in range(m):
        score_matrix[i][0] = indel * i

    for i in range(1, m):
        for j in range(1, n):
            score_matrix[i][j] = max(score_matrix[i][j-1]+indel, score_matrix[i-1][j]+indel, score_matrix[i-1][j-1]+diago[i-1][j-1])
    return score_matrix

def Backtracking(score):
    max_score = max(score[-1])
    sii = len(score)-1
    sij = score[-1].index(max_score)
    end_point = (sii, sij)

    route = ''
    while sii != 0:
        if score[sii][sij] == score[sii - 1][sij] + indel:
            route = 'd' + route
            sii = sii - 1

        elif score[sii][sij] == score[sii][sij-1] + indel:
            route = 'i' + route
            sij = sij - 1
        else:
            route = 'm' + route
            sii = sii - 1
            sij = sij - 1
    start_point = (sii, sij)
    return max_score, route, start_point, end_point

def route_to_alignment(str1, str2, route, start, end):
    align_str1 = ''
    align_str2 = ''
    new_str1 = str1[start[1]:end[1]]
    new_str2 = str2[start[0]:end[0]]
    index_1 = 0
    index_2 = 0
    for path in route:
        if path == 'm':
            align_str1 += new_str1[index_1]
            align_str2 += new_str2[index_2]
            index_1 += 1
            index_2 += 1
        elif path == 'i':
            align_str1 += new_str1[index_1]
            align_str2 += '-'
            index_1 += 1
        else:
            align_str1 += '-'
            align_str2 += new_str2[index_2]
            index_2 += 1

    print (align_str1)
    print (align_str2)

d = (matrix_maker(string_1, string_2, ATGC))
score = DP(d)
m, r, s, e = Backtracking(score)
print (m)
route_to_alignment(string_1, string_2, r, s, e)
