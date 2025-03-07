f = open("rosalind_ba3h.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]
k = data[0]
kmers = data[1:]

def make_graph(k, kmers):

    graph = {}
    for kmer in kmers:
        if kmer in graph:
            continue
        else:
            graph[kmer] = []

    for key in graph:
        for kmer in kmers:
            if key[1:] == kmer[:-1]:
                graph[key].append(kmer)
    return graph

def start_end(graph):

    in_and_out = []
    for key in graph:
        in_and_out.append([key, 0])
    
    for i in range(len(in_and_out)):
        in_and_out[i][1] -= len(graph[in_and_out[i][0]])
        for node in graph[in_and_out[i][0]]:
            for j in range(len(in_and_out)):
                if in_and_out[j][0] == node:
                    in_and_out[j][1] += 1
    
    for pair in in_and_out:
        if pair[1] == -1:
            start = pair[0]
            
        elif pair[1] == 1:
            end = pair[0]
            
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

    while arr_node != end_node:
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

def list_to_string(lst):

    sum_string = lst[0]
    for kmer in lst[1:]:
        sum_string = sum_string + kmer[-1]
    return sum_string
    
start, end = start_end(make_graph(k, kmers))
print (list_to_string(EulerianPath(start, end, make_graph(k, kmers))))