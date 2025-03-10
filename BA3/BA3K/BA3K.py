f = open("rosalind_ba3k.txt", 'r')
data = f.readlines()
for i in range(len(data)):
    data[i] = data[i].strip()

def debruijn_nodes(data):
    node = set()
    for line in data:
        node.add(line[1:])
        node.add(line[:-1])
    return node

def make_graph(nodes, data):
    graph = {}
    for node in nodes:
        graph[node] = []

    for edge in data:
        for key in graph:
            if key == edge[:-1]:
                graph[key].append(edge[1:])
    return graph

def in_and_out(graph):
    in_and_out = {}
    for key in graph:
        in_and_out[key] = [0, 0] # key: [in, out]
    for node in graph:
        in_and_out[node][1] = -len(graph[node])
        for arrival_node in graph[node]:
            in_and_out[arrival_node][0] += 1
    return in_and_out

graph = (make_graph(debruijn_nodes(data), data))
in_and_out_data = (in_and_out(graph))

def edgetocontig(edge):
    answer = edge[0]
    for node in edge[1:]:
        answer += node[-1]
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

def contig_lst_maker(graph):
    contig_lst = []
    while graph != {}:
        for key in list(graph):
            if in_and_out_data[key][0] != 1 or in_and_out_data[key][1] != -1:
                contig = contig_maker(graph, key)
                if contig == None:
                    continue
                else:
                    contig_lst.append(edgetocontig(contig))
    return contig_lst

w = open('output_ba3k.txt', 'w')
w.write(' '.join(map(str, contig_lst_maker(graph))))
w.close()