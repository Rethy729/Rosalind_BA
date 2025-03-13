f = open('rosalind_ba7e.txt', 'r')
data = f.readlines()

def data_processing(data):
    n = int(data[0])
    matrix = []
    for line in data[1:]:
        matrix.append(list(map(int, line.strip().split())))

    return n, matrix

n, matrix = data_processing (data)
original_matrix = matrix[:] # !!original matrix!!

internal_nodes = []
for i in range(n, 2*n-2):
    internal_nodes.append(i)

#print (internal_nodes)

def NJ (n, matrix, indices): #the index is the index order of matrix
    if n == 2:
        graph = []
        graph.append([indices[0], indices[1], matrix[0][1]])
        graph.append([indices[1], indices[0], matrix[1][0]])
        return graph

    #print (matrix)
    #nj-matrix = the neighbor-joining matrix constructed from the distance matrix
    nj_matrix = []
    for i in range(n):
        nj_matrix.append([0]*n)
    total_distance = []
    for i in range(n):
        total_distance.append(sum(matrix[i]))
    for i in range(n):
        for j in range(i+1, n):
            nj_matrix[i][j] = (n-2) * matrix[i][j] - (total_distance[i] + total_distance[j])
            nj_matrix[j][i] = nj_matrix[i][j]

    #find the elements i and j such that Dij* is a minimum non-diagonal element of D*
    min = 999999
    for i in range(n):
        for j in range(i + 1, n):
            if nj_matrix[i][j] < min:
                min = nj_matrix[i][j]
                i_p, j_p = i, j
                i_index, j_index = indices[i], indices[j]

    delta = (total_distance[i_p] - total_distance[j_p])/(n-2)
    limb_i = (matrix[i_p][j_p] + delta)/2
    limb_j = (matrix[i_p][j_p] - delta)/2

    #add a new row/column to D, using Dkm = Dmk = (Dki+Dkj-Dij)/2 for any k
    new_matrix = []
    for i in range(len(matrix)):
        if i == i_p or i == j_p:
            continue
        else:
            new_row = matrix[i][:i_p] + matrix[i][i_p + 1:j_p] + matrix[i][j_p+ 1:]
            new_matrix.append(new_row)

    indices_temp = indices[:]
    indices.remove(i_index)
    indices.remove(j_index)
    merge_row = []

    for i in indices:
        merge_row.append((matrix[i_p][indices_temp.index(i)] + matrix[j_p][indices_temp.index(i)] - matrix[i_p][j_p])/2)

    new_matrix.append(merge_row)
    merge_row.append(0)
    for i in range(len(new_matrix) - 1):
        new_matrix[i].append(merge_row[i])

    indices.append(internal_nodes[4-n])
    new_indices = indices
    #print (new_indices)

    edge_lower = NJ(n-1, new_matrix, new_indices)

    edge_lower.append([internal_nodes[4 - n], i_index, limb_i])
    edge_lower.append([i_index,internal_nodes[4-n],limb_i])
    edge_lower.append([internal_nodes[4 - n], j_index, limb_j])
    edge_lower.append([j_index, internal_nodes[4-n], limb_j])

    edge_lower.sort()
    return edge_lower

index = []
for i in range(n):
    index.append(i)
#print (index)

answer = NJ(n, matrix, index)
for edge in answer:
    weight = round(edge[2], 3)
    print(str(edge[0])+'->'+str(edge[1])+':'+f'{weight:.03f}')