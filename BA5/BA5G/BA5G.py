f = open('rosalind_ba5g.txt', 'r')
data = f.readlines()
string_1 = data[0].strip()
string_2 = data[1].strip()

def edit_distance(str1, str2):
    seq1 = 'X' + str1
    seq2 = 'X' + str2
    n = len(seq1)
    m = len(seq2)

    matrix = []
    for i in range(m):
        matrix.append([0] * n)

    for i in range(m):
        matrix[i][0] = i
    for i in range(n):
        matrix[0][i] = i

    for i in range(1, m):
        for j in range(1, n):
            if seq1[j] == seq2[i]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

    return matrix[-1][-1]

print (edit_distance(string_1, string_2))