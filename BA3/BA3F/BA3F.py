f = open("rosalind_ba3f.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]
edge_data = []
for line in data:
    edge = list(map(str, line.split(' -> ')))
    edge_data.append(edge)
    
graph = {}
for edge in edge_data:
    graph[int(edge[0])] = list(map(int, edge[1].split(',')))

def find_cycle(start_node, graph):

    cycle = []
    arr_node = graph[start_node].pop()   #pop in dictionary, the first "walk"

    while arr_node != start_node:         #while the arrival node != start node, which means it forms a loop
        cycle.append(arr_node)            #append the arrival node
        arr_node = graph[arr_node].pop()  #next "walk"
    cycle.append(arr_node)                #append the last arrival node, which is same as start_node

    for key in list(graph):               #delete the empty key
        if graph[key] == []:
            del graph[key]
    
    return cycle                          #eventually, the cycle is like this (start_node = 1 -> [2, 4, 6, 8, 3, 1] (1 is not included in the beginning)

def EulerianCycle(start_node, graph):
    cycle = [start_node] + find_cycle(start_node, graph)       #start from an initial loop, which includes the start node at the beginning
    break_bool = True
    while break_bool:
        break_bool = False
        for i, node in enumerate(cycle):
            if node in graph:                                  #finding an unused edge starting from some node in cycle
                break_bool = True                              #if no unused edge, break_bool does not change to True, while loop eventually breaks
                cycle = cycle[:i+1] + find_cycle(node, graph) + cycle[i+1:]
                break
    return cycle

answer = EulerianCycle(0, graph)

w = open('output_ba3f.txt', 'w')
w.write('->'.join(map(str, answer)))
w.close()
