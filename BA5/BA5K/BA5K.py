f = open('BLOSUM62.txt', 'r')
data = f.readlines()
char_lst = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','-']
BLOSUM62 = []
for line in data[1:]:
    BLOSUM62.append(list(map(int, line.split())))
#print (BLOSUM62)

f = open('rosalind_ba5k.txt', 'r')
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

def MidNode(diago):
    n = len(diago[0]) + 1  # the horizontal length of the matrix
    m = len(diago) + 1  # the vertical length of the matrix
    score_matrix = []

    for i in range(m):
        score_matrix.append([-99999999] * n)

    for i in range(n):
        score_matrix[0][i] = (indel) * i

    for i in range(m):
        score_matrix[i][0] = (indel) * i

    for i in range(1, m):
        for j in range(1, n):
            score_matrix[i][j] = max(score_matrix[i - 1][j] + indel, score_matrix[i][j - 1] + indel,
                                     score_matrix[i - 1][j - 1] + diago[i - 1][j - 1])
    middle = len(diago[0])//2

    middle_column = []
    for i in range(m):
        middle_column.append(score_matrix[i][middle])
    max_score = max(middle_column)
    middle_node = [middle_column.index(max_score), middle]
    print (middle_node)

    route = ''
    sii = len(score_matrix)-1 #sii = start_index_i
    sij = len(score_matrix[0])-1 #sij = start_index_j

    while sii != middle_node[0] and sij != middle_node[1]:
        if score_matrix[sii][sij] == score_matrix[sii-1][sij] + indel:
            route = 'd' + route
            sii = sii - 1
        elif score_matrix[sii][sij] == score_matrix[sii][sij-1] + indel:
            route = 'i' + route
            sij = sij - 1
        else:
            route = 'm' + route
            sii = sii - 1
            sij = sij - 1
    if route[0] == 'm':
        next_node = [middle_node[0]+1, middle_node[1]+1]
    elif route[0] == 'd':
        next_node = [middle_node[0]+1, middle_node[1]]
    else:
        next_node = [middle_node[0], middle_node[1]+1]
    print (next_node)

string_1, string_2 = string_2, string_1
(MidNode(matrix_maker(string_1, string_2, BLOSUM62)))
