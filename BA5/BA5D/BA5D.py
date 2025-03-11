f = open("rosalind_ba5d.txt", 'r')
data = f.readlines()
source = int(data[0])
sink = int(data[1])

def graph_gen(data):
    graph = {}
    for line in data[2:]:
        edge = list(map(str, line.strip().split('->')))
        if int(edge[0]) not in graph:
            weight = {}
            weight[list(map(int, edge[1].split(':')))[0]] = list(map(int, edge[1].split(':')))[1]
            graph[int(edge[0])] = weight
        else:
            graph[int(edge[0])][list(map(int, edge[1].split(':')))[0]] = list(map(int, edge[1].split(':')))[1]
    return graph

def longest_path(graph):
    nodes = []
    for key in graph:
        nodes.append(key)
        for key_2 in graph[key]:
            nodes.append(key_2)
    max_node = max(nodes)

    distance = [-1]*(max_node+1)
    route = []
    for i in range(max_node+1): #route = [[], [], [], ...., []]
        route.append([])

    distance[source] = 0
    route[source].append(source)

    expected_search = []  #the first node to visit
    expected_search.append(source)

    while expected_search != []:
        next_expected_search = []
        for start_node in expected_search:
            if start_node in graph:

                for key in graph[start_node]: #the next node to visit
                    next_expected_search.append(key)

                for arr_node in graph[start_node]:
                    distance_temp = distance[arr_node]
                    distance[arr_node] = max(distance[arr_node], distance[start_node]+graph[start_node][arr_node])
                    if distance_temp == distance[arr_node]:
                        continue
                    else:
                        new_route = route[start_node][:]
                        new_route.append(arr_node)
                        route[arr_node] = new_route
        expected_search = list(set(next_expected_search))

    return distance[sink], route[sink]

dis, root = (longest_path(graph_gen(data)))
print(dis)
print('->'.join(map(str, root)))