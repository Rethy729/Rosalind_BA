f = open('BLOSUM62.txt', 'r')
data = f.readlines()
char_lst = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','-']
BLOSUM62 = []
for line in data[1:]:
    BLOSUM62.append(list(map(int, line.replace('  ', ' ').split(' '))))
#print (BLOSUM62)

f = open('rosalind_ba5e.txt', 'r')
data = f.readlines()
string_1 = (list(map(str, data[0].strip())))
string_2 = (list(map(str, data[1].strip())))

def matrix_maker(str1, str2, score): #str1 is horizontal, str2 is vertical
    hori = []
    verti = []
    diago = []

    for i in range(len(str2)+1):
        hori.append([-5]*len(str1))
    for i in range(len(str1)+1):
        verti.append([-5]*len(str2))
    for i in range(len(str2)):
        diago_row = []
        char_2 = str2[i]
        char_2_index = char_lst.index(char_2)
        for j in range(len(str1)):
            char_1 = str1[j]
            char_1_index = char_lst.index(char_1)
            diago_row.append(score[char_1_index][char_2_index])
        diago.append(diago_row)

    return hori, verti, diago

def DP(hori, verti, diago):
    n = len(verti) #the horizontal length of the matrix
    m = len(hori) #the vertical length of the matrix
    score_matrix = []
    #route_matrix = []
    for i in range(m):
        score_matrix.append([-99999999]*n)
        #route_matrix_row = []
        #for j in range(n):
            #route_matrix_row.append('')
        #route_matrix.append(route_matrix_row)

    for i in range(n):
        score_matrix[0][i] = (-5)*i
        #route_matrix[0][i] = 'i'*i
    for i in range(m):
        score_matrix[i][0] = (-5)*i
        #route_matrix[i][0] = 'd'*i

    for i in range(1, m):
        for j in range(1, n):
            score_matrix[i][j] = max(score_matrix[i-1][j]-5, score_matrix[i][j-1]-5, score_matrix[i-1][j-1]+diago[i-1][j-1])
            #if score_matrix[i][j] == score_matrix[i-1][j]-5:
                #route_matrix[i][j] = route_matrix[i-1][j] + 'd'
           #elif score_matrix[i][j] == score_matrix[i][j-1]-5:
                #route_matrix[i][j] = route_matrix[i][j-1] + 'i'
            #else:
                #route_matrix[i][j] = route_matrix[i-1][j-1] + 'm'

    #return score_matrix[m-1][n-1], route_matrix[m-1][n-1]
    return score_matrix[m - 1][n - 1]

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

h, v, d = (matrix_maker(string_1, string_2, BLOSUM62))
max_score = DP(h, v, d)
print (max_score)
#route_to_alignment(string_1, string_2, route)
