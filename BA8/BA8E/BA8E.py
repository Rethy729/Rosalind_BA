f = open('rosalind_ba8e.txt', 'r')
data = f.readlines()

def data_processing(data):
    n = int(data[0])
    matrix = []
    for line in data[1:]:
        matrix.append(list(map(float, line.strip().split())))

    return n, matrix

n, matrix = data_processing (data)
original_matrix = matrix[:] # !!original matrix!!

def matrix_convert(matrix, matrix_ori, cluster, index_i, index_j): #cluster  = [[0], [1], [2,3], [4]] // i, j sorting not needed
    if index_i>index_j:
        index_i, index_j = index_j, index_i #always, i<j

    merge_i = cluster[index_i]
    merge_j = cluster[index_j]
    cluster.remove(merge_i)
    cluster.remove(merge_j)
    cluster.append(merge_i + merge_j)

    new_matrix = []
    for i in range(len(matrix)):
        if i == index_i or i == index_j:
            continue
        else:
            new_row = matrix[i][:index_i] + matrix[i][index_i + 1:index_j] + matrix[i][index_j + 1:]
            new_matrix.append(new_row)

    merge_row = []
    new_cluster = cluster[-1]  # ex) [0, 2, 3]

    for i in range(len(new_matrix)):
        cluster_1 = cluster[i]
        edge_count = 0
        distance_sum = 0
        for node_1 in cluster_1:
            for node_new in new_cluster:
                distance_sum += matrix_ori[node_1][node_new]
                edge_count += 1

        merge_row.append(distance_sum / edge_count)

    #print (merge_row)
    new_matrix.append(merge_row)
    merge_row.append(0)
    for i in range(len(new_matrix) - 1):
        new_matrix[i].append(merge_row[i])
    return cluster, new_matrix

def HC(matrix, n):

    clusters = []
    for i in range(n):
        clusters.append([i])

    while len(clusters) != 1:
        #print (matrix)
        min = 999999
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                if matrix[i][j]<min:
                    min = matrix[i][j]
                    i_index, j_index = i, j

        new_cluster = clusters[i_index] + clusters[j_index]

        new_cluster_for_printing = new_cluster[:]
        for i in range(len(new_cluster_for_printing)):
            new_cluster_for_printing[i] = new_cluster_for_printing[i]+1

        print(' '.join(map(str, new_cluster_for_printing)))

        new_clusters, new_matrix = matrix_convert(matrix, original_matrix, clusters, i_index, j_index)
        clusters = new_clusters
        matrix = new_matrix

HC(matrix, n)