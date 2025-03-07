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
    arr_node = graph[start_node].pop()

    while arr_node != start_node:
        cycle.append(arr_node)          
        arr_node = graph[arr_node].pop()
    cycle.append(arr_node)

    for key in list(graph):
        if graph[key] == []:
            del graph[key]
    
    return cycle


def EulerianCycle(start_node, graph):
    cycle = [start_node] + find_cycle(start_node, graph)

    break_bool = True
    while break_bool:
        break_bool = False
        for i, node in enumerate(cycle):
            if node in graph:
                break_bool = True
                cycle = cycle[:i+1] + find_cycle(node, graph) + cycle[i+1:]
                break

    return cycle

answer = EulerianCycle(0, graph)

w = open('output_ba3f.txt', 'w')
w.write('->'.join(map(str, answer)))
w.close()
