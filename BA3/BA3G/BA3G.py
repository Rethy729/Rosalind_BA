f = open("rosalind_ba3g.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]
edge_data = []
for line in data:
    edge = list(map(str, line.split(' -> ')))
    edge_data.append(edge)
    
graph = {}
for edge in edge_data:
    graph[int(edge[0])] = list(map(int, edge[1].split(',')))

def start_end(graph): #Determines the start node & ending node, using the property that these nodes are not balanced. (has to be -1 or +1)

    key_list = list(graph)
    value_list = []
    for key in graph:
        value_list += graph[key]
    max_node = max(key_list+value_list)
    
    in_and_out = [0]*(max_node+1)

    for key in graph:
        in_and_out[key] -= len(graph[key])
        for node in graph[key]:
            in_and_out[node] += 1

    for i, value in enumerate(in_and_out):
        if value == -1:
            start = i
        elif value == +1:
            end = i
    return start, end

def find_cycle(start_node, graph):

    cycle = []
    arr_node = graph[start_node].pop()

    while arr_node != start_node:
        cycle.append(arr_node)          
        arr_node = graph[arr_node].pop()
    cycle.append(arr_node)

    for key in list(graph):
        if graph[key] == []:
            del graph[key]
    
    return cycle

def EulerianPath(start_node, end_node, graph):
    cycle = [start_node]
    arr_node = graph[start_node].pop()

    while arr_node != end_node:    #The initial "path" starting from start_node and ends at the end_node
        cycle.append(arr_node)
        arr_node = graph[arr_node].pop()
    cycle.append(arr_node)

    for key in list(graph):
        if graph[key] == []:
            del graph[key]

    break_bool = True
    while break_bool:
        break_bool = False
        for i, node in enumerate(cycle):
            if node in graph:
                break_bool = True
                cycle = cycle[:i+1] + find_cycle(node, graph) + cycle[i+1:]
                break
    return cycle

start, end = start_end(graph)
answer = EulerianPath(start, end, graph)

w = open('output_ba3g.txt', 'w')
w.write('->'.join(map(str, answer)))
w.close()
