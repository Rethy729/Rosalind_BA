f = open('BLOSUM62.txt', 'r')
data = f.readlines()
char_lst = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','-']
BLOSUM62 = []
for line in data[1:]:
    BLOSUM62.append(list(map(int, line.split())))
#print (BLOSUM62)

f = open('rosalind_ba5e.txt', 'r')
data = f.readlines()
string_1 = (list(map(str, data[0].strip())))
string_2 = (list(map(str, data[1].strip())))

indel = -5 #score of indel

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
        score_matrix[0][i] = (indel)*i

    for i in range(m):
        score_matrix[i][0] = (indel)*i

    for i in range(1, m):
        for j in range(1, n):
            score_matrix[i][j] = max(score_matrix[i-1][j]+indel, score_matrix[i][j-1]+indel, score_matrix[i-1][j-1]+diago[i-1][j-1])

    return score_matrix

def Backtracking(score):
    route = ''
    sii = len(score)-1 #sii = start_index_i
    sij = len(score[0])-1 #sij = start_index_j

    while sii != 0 and sij != 0:
        if score[sii][sij] == score[sii-1][sij] + indel:
            route = 'd' + route
            sii = sii - 1
        elif score[sii][sij] == score[sii][sij-1] + indel:
            route = 'i' + route
            sij = sij - 1
        else:
            route = 'm' + route
            sii = sii - 1
            sij = sij - 1
    for i in range(sii):
        route = 'd' + route
    for i in range(sij):
        route = 'i' + route
    return route

def route_to_alignment(str1, str2, route):
    align_str1 = ''
    align_str2 = ''
    index_1 = 0
    index_2 = 0
    for path in route:
        if path == 'm':
            align_str1 += str1[index_1]
            align_str2 += str2[index_2]
            index_1 += 1
            index_2 += 1
        elif path == 'i':
            align_str1 += str1[index_1]
            align_str2 += '-'
            index_1 += 1
        else:
            align_str1 += '-'
            align_str2 += str2[index_2]
            index_2 += 1
    print (align_str1)
    print (align_str2)

d = (matrix_maker(string_1, string_2, BLOSUM62))
score = DP(d)
print (score[-1][-1])
route_to_alignment(string_1, string_2, Backtracking(score))

