f = open('rosalind_ba7b.txt', 'r')
data = f.readlines()

def data_processing(data):
    n = int(data[0])
    j = int(data[1])
    matrix = []
    for line in data[2:]:
        matrix.append(list(map(int, line.strip().split())))

    return n, j, matrix

n, j, matrix = data_processing (data)

def limb_length(n, j, matrix):

    ik_pair = []
    for a in range(n):
        if a == j:
            continue

        for b in range(n):
            if b == j:
                continue
            ik_pair.append([a, b])

    min_limb_length = 9999999999
    for pair in ik_pair:

        i = pair[0]
        k = pair[1]
        limb_length = (matrix[i][j] + matrix[j][k] - matrix[i][k])/2
        if limb_length < min_limb_length:
            min_limb_length = limb_length

    return (min_limb_length)

print (int(limb_length(n, j, matrix)))
