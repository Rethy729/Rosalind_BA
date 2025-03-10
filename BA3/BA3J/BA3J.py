f = open("rosalind_ba3j.txt", 'r')
data = f.readlines()
k = list(map(int, data[0].split(' ')))[0]
d = list(map(int, data[0].split(' ')))[1]

def debruijn(data):
    db_nodes = []
    for line in data[1:]:
        prefix = []
        suffix = []
        kdmer_lst = list(map(str, line.strip().split('|')))
        prefix.append(kdmer_lst[0][:-1])
        prefix.append(kdmer_lst[1][:-1])
        suffix.append(kdmer_lst[0][1:])
        suffix.append(kdmer_lst[1][1:])
        db_nodes.append(tuple(prefix))
        db_nodes.append(tuple(suffix))

    return list(set(db_nodes))

def make_graph (read_data):
    graph = {}
    for pair in read_data:
        if pair in graph:
            continue
        else:
            graph[pair] = []

    for key in graph:
        for pair in read_data:
            if key[0][1:] == pair[0][:-1] and key[1][1:] == pair[1][:-1]:
                graph[key].append(pair)
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

    start_end = [0, 0]
    for pair in in_and_out:
        if pair[1] == -1:
            start_end[0] = pair[0]
        elif pair[1] == 1:
            start_end[1] = pair[0]
            
    return start_end

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
    sum_prefix_lst = []
    sum_suffix_lst = []

    for i in range(len(lst)-1):
        sum_prefix_lst.append(lst[i][0]+lst[i+1][0][-1])
        sum_suffix_lst.append(lst[i][1]+lst[i+1][1][-1])

    prefix_str = sum_prefix_lst[0]
    suffix_str = sum_suffix_lst[0]

    for string in sum_prefix_lst[1:]:
        prefix_str += string[-1]

    for string in sum_suffix_lst[1:]:
        suffix_str += string[-1]

    match = 2*(k+len(sum_prefix_lst)-1) - ((2*k)+d+len(lst)-2)
    return prefix_str + suffix_str[match:]

#print (debruijn(data))
#print (make_graph(debruijn(data)))
#print (start_end(make_graph(debruijn(data))))
#print (EulerianPath(start_end(make_graph(debruijn(data)))[0], start_end(make_graph(debruijn(data)))[1],make_graph(debruijn(data))))
print (list_to_string(EulerianPath(start_end(make_graph(debruijn(data)))[0], start_end(make_graph(debruijn(data)))[1],make_graph(debruijn(data)))))
