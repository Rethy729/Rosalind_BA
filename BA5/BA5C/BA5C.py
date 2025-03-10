f = open("rosalind_ba5c.txt", 'r')
data = f.readlines()
DNA_seq = []
for line in data:
    DNA_seq.append(line.strip())

def LCS(seq1, seq2):
    seq1 = 'X' + seq1
    seq2 = 'X' + seq2
    n = len(seq1)
    m = len(seq2)

    matrix = []
    for i in range(m):
        matrix.append([''] * n)

    for i in range(m):
        for j in range(n):
            if seq1[j] == 'X' or seq2[i] == 'X':
                continue

            elif seq1[j] == seq2[i]:
                matrix[i][j] = matrix[i - 1][j - 1] + seq2[i]

            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)

    return matrix[-1][-1]

print(LCS(DNA_seq[0], DNA_seq[1]))