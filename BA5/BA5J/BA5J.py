f = open('BLOSUM62.txt', 'r')
data = f.readlines()
char_lst = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','-']
BLOSUM62 = []
for line in data[1:]:
    BLOSUM62.append(list(map(int, line.split())))
#print (BLOSUM62)

f = open('rosalind_ba5j.txt', 'r')
data = f.readlines()
string_1 = (list(map(str, data[0].strip())))
string_2 = (list(map(str, data[1].strip())))

gop = -11 #gop = gap opening penalty
gep = -1 #gep = gap extension penalty

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

    lower_matrix = [] #vertical gap
    middle_matrix = [] #digonal gap
    upper_matrix = [] #horizontal gap

    for i in range(m):
        lower_matrix.append([-99999999] * n)
        middle_matrix.append([-99999999] * n)
        upper_matrix.append([-99999999] * n)

    middle_matrix[0][0] = 0
    middle_matrix[0][1] = gop
    middle_matrix[1][0] = gop
    lower_matrix[0][0] = 0
    upper_matrix[0][0] = 0
    lower_matrix[1][0] = gop
    upper_matrix[0][1] = gop

    for i in range(2, n):
        upper_matrix[0][i] = upper_matrix[0][i-1]+gep
        middle_matrix[0][i] = upper_matrix[0][i]
    for i in range(2, m):
        lower_matrix[i][0] = lower_matrix[i-1][0]+gep
        middle_matrix[i][0] = lower_matrix[i][0]

    for i in range(1, m):
        for j in range(1, n):
            lower_matrix[i][j] = max(lower_matrix[i-1][j] + gep, middle_matrix[i-1][j] + gop)
            upper_matrix[i][j] = max(upper_matrix[i][j-1] + gep, middle_matrix[i][j-1] + gop)
            middle_matrix[i][j] = max(lower_matrix[i][j], upper_matrix[i][j], middle_matrix[i-1][j-1] + diago[i-1][j-1])


    return lower_matrix, middle_matrix, upper_matrix

def Backtracking(lower, middle, upper):
    route = ''
    score = middle[-1][-1]
    sii = len(middle) - 1  # sii = start_index_i
    sij = len(middle[0]) - 1  # sij = start_index_j

    while sii != 0 and sij != 0:
        if middle[sii][sij] == lower[sii][sij]:
            while lower[sii][sij] == lower[sii-1][sij] + gep:
                route = 'd' + route
                sii -= 1
            route = 'd' + route
            sii -= 1
        elif middle[sii][sij] == upper[sii][sij]:
            while upper[sii][sij] == upper[sii][sij-1] + gep:
                route = 'i' + route
                sij -= 1
            route = 'i' + route
            sij -= 1
        else:
            route = 'm' + route
            sii -= 1
            sij -= 1
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
l, m, d = DP(d)
r = Backtracking(l, m, d)
print(m[-1][-1])
route_to_alignment(string_1, string_2, r)