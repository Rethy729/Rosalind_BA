f = open("rosalind_ba3m.txt", 'r')
data = f.readlines()

def make_graph(data): #{1: [2], 2: [3], 3: [4, 5], 6: [7], 7: [6]}
    graph = {}
    for line in data:
        edge = list(map(str, line.strip().split(' -> ')))
        graph[int(edge[0])] = list(map(int, edge[1].split(',')))
    return graph

def in_and_out(graph):
    in_and_out = {}
    for key in graph:
        in_and_out[key] = [0, 0] # key: [in, out]
        for arr in graph[key]:
            in_and_out[arr] = [0, 0]

    for node in graph:
        in_and_out[node][1] = -len(graph[node])
        for arrival_node in graph[node]:
            in_and_out[arrival_node][0] += 1
    return in_and_out

graph = (make_graph(data))
in_and_out_data = (in_and_out(graph))

def edgetocontig(edge):
    answer = str(edge[0])
    for node in edge[1:]:
        answer += ' '+str(node)
    return answer

def contig_maker(graph, start_node):
    contig = [start_node]
    if in_and_out_data[start_node][1] == 0:
        return
    else:
        arr_node = graph[start_node].pop()

        while in_and_out_data[arr_node][0] == 1 and in_and_out_data[arr_node][1] == -1:
            contig.append(arr_node)
            arr_node = graph[arr_node].pop()
        contig.append(arr_node)

        for key in list(graph): #list(graph) -> to aviod dictionary size change during iteration
            if graph[key] == []:
                del graph[key]
    return contig

def loop_determinate (graph, start_node):
    arr_node = graph[start_node][0]
    while in_and_out_data[arr_node][0] == 1 and in_and_out_data[arr_node][1] == -1:
        arr_node = graph[arr_node][0]
        if arr_node == start_node:

            return True
    return False

def contig_maker_loop(graph, start_node):
    contig_loop = [start_node]

    if loop_determinate(graph, start_node) == True:
        arr_node = graph[start_node].pop()
        while arr_node != start_node:
            contig_loop.append(arr_node)
            arr_node = graph[arr_node].pop()
        contig_loop.append(arr_node)
        for key in list(graph):  # list(graph) -> to aviod dictionary size change during iteration
            if graph[key] == []:
                del graph[key]
        return contig_loop
    else:
        return

def contig_lst_maker(graph):
    contig_lst = []
    while graph != {}:
        for key in list(graph):#first, take care of isolated loops
            if key not in graph:
                continue
            if in_and_out_data[key][0] == 1 and in_and_out_data[key][1] == -1:
                contig_loop = contig_maker_loop(graph, key)
                if contig_loop == None:
                    continue
                else:
                    contig_lst.append(edgetocontig(contig_loop))
        for key in list(graph):
            if in_and_out_data[key][0] != 1 or in_and_out_data[key][1] != -1:
                contig = contig_maker(graph, key)
                if contig == None:
                    continue
                else:
                    contig_lst.append(edgetocontig(contig))

    return contig_lst

w = open('output_ba3m.txt', 'w')
for line in contig_lst_maker(graph):
    w.write(line.replace(' ', ' -> ')+'\n')
w.close()