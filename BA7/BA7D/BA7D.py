f = open('rosalind_ba7d.txt', 'r')
data = f.readlines()

def data_processing(data):
    n = int(data[0])
    matrix = []
    for line in data[1:]:
        matrix.append(list(map(int, line.strip().split())))

    return n, matrix

n, matrix = data_processing (data)
original_matrix = matrix[:] # !!original matrix!!
max_node = n+2 #0 to 6

def matrix_convert(matrix, matrix_ori, cluster, index_i, index_j): #cluster  = [[0], [1], [2,3], [4]] // i, j sorting not needed
    if index_i>index_j:
        index_i, index_j = index_j, index_i #always, i<j

    merge_i = cluster[index_i]
    merge_j = cluster[index_j]
    cluster.remove(merge_i)
    cluster.remove(merge_j)
    cluster.append(merge_i+merge_j)

    new_matrix = []
    for i in range(len(matrix)):
        if i == index_i or i == index_j:
            continue
        else:
            new_row = matrix[i][:index_i] + matrix[i][index_i+1:index_j] + matrix[i][index_j+1:]
            new_matrix.append(new_row)

    merge_row = []
    new_cluster = cluster[-1] #ex) [0, 2, 3]

    for i in range(len(new_matrix)):
        cluster_1 = cluster[i]
        edge_count = 0
        distance_sum = 0
        for node_1 in cluster_1:
            for node_new in new_cluster:
                distance_sum += matrix_ori[node_1][node_new]
                edge_count += 1

        merge_row.append(distance_sum/edge_count)

    new_matrix.append(merge_row)
    merge_row.append(0)
    for i in range(len(new_matrix)-1):
        new_matrix[i].append(merge_row[i])

    return cluster, new_matrix

(matrix_convert([[0, 20, 14.0], [20, 0, 16.5], [14.0, 16.5, 0]], original_matrix, [[0], [1], [2, 3]], 0, 2))

def UPGMA(n, matrix):

    clusters = []
    for i in range(n):
        clusters.append([i])

    internal_node_index = n
    clusters_data = {} # {(0, 1, 2):[4(index), 8(age)]}

    for i in range(len(clusters)):
        clusters_data[tuple(clusters[i])] = [i, 0]
    edges = []

    while len(clusters) != 1:

        min = 999999
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                if matrix[i][j]<min:
                    min = matrix[i][j]
                    i_index, j_index = i, j

        internal_node_age = min/2
        new_cluster = clusters[i_index] + clusters[j_index]
        clusters_data[tuple(new_cluster)] = [internal_node_index, internal_node_age]

        a, b = internal_node_index, internal_node_age
        c, d = clusters_data[tuple(clusters[i_index])][0], clusters_data[tuple(clusters[i_index])][1]
        e, f = clusters_data[tuple(clusters[j_index])][0], clusters_data[tuple(clusters[j_index])][1]

        edges.append([a, c, (b-d)])
        edges.append([c, a, (b-d)])
        edges.append([a, e, (b-f)])
        edges.append([e, a, (b-f)])

        new_clusters, new_matrix = matrix_convert(matrix, original_matrix, clusters, i_index, j_index)
        internal_node_index += 1
        clusters = new_clusters
        matrix = new_matrix
        #print(matrix)
    edges.sort()
    return edges

answer = UPGMA(n, matrix)
for edge in answer:
    weight = round(edge[2], 3)
    print(str(edge[0])+'->'+str(edge[1])+':'+f'{weight:.03f}')

    #the point, making a new_matrix -> we have to compute the al node distance sum and get an average
    #ex) [0, 1] - [2, 4] -> (D(0, 2)+D(0, 4)+D(1, 2)+D(1, 4))/4 (=2x2)