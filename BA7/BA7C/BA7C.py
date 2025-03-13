from collections import deque
f = open('rosalind_ba7c.txt', 'r')
data = f.readlines()

def data_processing(data):
    n = int(data[0])
    matrix = []
    for line in data[1:]:
        matrix.append(list(map(int, line.strip().split())))

    return n, matrix

n, matrix = data_processing (data)
internal_nodes = []
for i in range(n, 2*n-2):
    internal_nodes.append(i)

#print (n, matrix)
def limb(matrix, n, j): #n is the length of matrix, j is the index of row which we will compute the limb function, (0_indexed)
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

    return min_limb_length

def additive_phylogeny(matrix, n):
    if n == 2:
        graph = []
        graph.append([0, 1, matrix[0][1]])
        graph.append([1, 0, matrix[1][0]])
        return graph
    #print (matrix)
    limb_length = limb(matrix, n, n-1)
    #print (limb_length)
    for i in range(n-1): #from 0 to n-2 (0_indexing) (when n-1, zero)
        matrix[n-1][i] = matrix[n-1][i] - int(limb_length)
        matrix[i][n-1] = matrix[n-1][i]

    #now, matrix is bald
    #print (matrix)
    three_leaves = [-1, -1, -1]
    for i in range(n-1):
        for j in range(i+1, n-1):
            if j == i:
                continue
            if matrix[n-1][i] + matrix[n-1][j] == matrix[i][j]:
                three_leaves = [i, n-1, j]
                break
        if three_leaves != [-1, -1, -1]:
            break
    #print (three_leaves)
    x = matrix[three_leaves[0]][three_leaves[1]]
    #recursive
    edge_minus = additive_phylogeny(matrix, n-1)
    #print (edge_minus)

    #compute and get a route i from j based on graph_minus
    #should be like this: [i, node1, node2, node3 ... , j]
    #also, the distance lst should be provided: [0, d1, d2, d3 ...  , dj]
    #and find the dn, dm pair which is dn<x<dm
    #node dn-dm should break
    #additional node: [nodei, newnode = internal_nodes[n-3], x-dn], [newnode, nodem, dm-x], [n-1, newnode, int(limb_length)]

    def graph(edges):
        max_node = 0
        for line in edges:
            if line[0] > max_node:
                max_node = line[0]
            if line[1] > max_node:
                max_node = line[1]

        graph = {}  # {0:{1:20, 3:30}, 1:{0:20} , ... }
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]][edge[1]] = edge[2]
            else:
                graph[edge[0]] = {edge[1]: edge[2]}
        return max_node, graph

    max_node, graph_minus = graph(edge_minus)

    def BFS(start_node, end_node, max_node, graph):

        distance_lst = [-1] * (max_node + 1)
        distance_lst[start_node] = 0
        route = [''] * (max_node + 1)
        route[start_node] = str(start_node)
        bfs_queue = deque()
        bfs_queue.append(start_node)
        while bfs_queue:
            v = bfs_queue.popleft()
            if v in graph:
                for arr_node in graph[v]:
                    if distance_lst[arr_node] == -1:
                        bfs_queue.append(arr_node)
                        distance_lst[arr_node] = distance_lst[v] + graph[v][arr_node]
                        route[arr_node] = route[v] + ' ' + str(arr_node)
        route_to_end = list(map(int, route[end_node].split()))
        distance_to_end = []
        for node in route_to_end:
            distance_to_end.append(distance_lst[node])

        return route_to_end, distance_to_end
    route, distance = BFS(three_leaves[0], three_leaves[2], max_node, graph_minus)

    for i in range(len(distance)-1):
        if distance[i] < x and distance[i+1] > x:
            node_n = route[i]
            node_m = route[i+1]
            dn = distance[i]
            dm = distance[i+1]

    edge_minus_temp = edge_minus[:]
    for edge in edge_minus_temp:
        if edge[0] == node_n and edge[1] == node_m:
            edge_minus.remove(edge)
        if edge[0] == node_m and edge[1] == node_n:
            edge_minus.remove(edge)

    edge_minus.append([node_n, internal_nodes[n-3], x-dn])
    edge_minus.append([internal_nodes[n-3], node_n, x-dn])
    edge_minus.append([internal_nodes[n-3], node_m, dm-x])
    edge_minus.append([node_m, internal_nodes[n-3], dm-x])
    edge_minus.append([n-1, internal_nodes[n-3], int(limb_length)])
    edge_minus.append([internal_nodes[n - 3], n-1, int(limb_length)])

    return edge_minus

answer = (additive_phylogeny(matrix, n))
answer.sort()
for edge in answer:
    print(str(edge[0])+'->'+str(edge[1])+':'+str(edge[2]))