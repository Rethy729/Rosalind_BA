from collections import deque

f = open('rosalind_ba7a.txt', 'r')
data = f.readlines()

def graph(data):
    n = int(data[0])
    edges = []
    for line in data[1:]:
        temp_edge = []
        lst = list(map(str, line.strip().split('->')))

        temp_edge.append(int(lst[0]))
        temp_edge.append(list(map(int, lst[1].split(':')))[0])
        temp_edge.append(list(map(int, lst[1].split(':')))[1])
        edges.append(temp_edge)

    max_node = 0
    for edge in edges:
        if edge[0]>max_node:
            max_node = edge[0]
        if edge[1]>max_node:
            max_node = edge[1]
    #print(max_node)

    graph = {} #{0:{1:20, 3:30}, 1:{0:20} , ... }
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]][edge[1]] = edge[2]
        else:
            graph[edge[0]] = {edge[1]:edge[2]}
    #print (graph)

    return n, max_node, graph

#we can use just BFS(queue) instead of dij because in a tree, a path from i to j is unique
def BFS(max_node, graph, pivot):
    distance_lst = [-1] * (max_node+1)

    bfs_queue = deque()
    distance_lst[pivot] = 0
    bfs_queue.append(pivot)

    while bfs_queue:
        v = bfs_queue.popleft()
        if v in graph:
            for arr_node in graph[v]:
                if distance_lst[arr_node] == -1:
                    bfs_queue.append(arr_node)
                    distance_lst[arr_node] = distance_lst[v] + graph[v][arr_node]
    return distance_lst

n, max_node, tree = graph(data)
#print (n)
print (tree)
#print (BFS(max_node, tree, 3))

def make_matrix(n, max_node, tree):
    matrix = []
    for i in range(n):
        matrix.append(BFS(max_node, tree, i)[:n])
    return matrix

for line in make_matrix(n, max_node, tree):
    print(' '.join(map(str, line)))



