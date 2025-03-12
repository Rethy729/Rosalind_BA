from collections import deque

f = open('rosalind_ba6c.txt', 'r')
data = f.readlines()

def data_processing(data):
    chromosome_lst_1 = list(map(str, data[0][1:-2].split(')(')))
    chromosome_lst_2 = list(map(str, data[1][1:-2].split(')(')))
    chromosome_1 = []
    chromosome_2 = []
    for chr in chromosome_lst_1:
        chromosome_temp = list(map(int, chr.split(' ')))
        chromosome_1.append(chromosome_temp)
    for chr in chromosome_lst_2:
        chromosome_temp = list(map(int, chr.split(' ')))
        chromosome_2.append(chromosome_temp)
    BLOCK = 0
    for line in chromosome_1:
        BLOCK += len(line)

    return BLOCK, chromosome_1, chromosome_2

block, chr_1, chr_2 = data_processing(data)

#print (block) #total element number
#print (chr_1) #[[1, 2, 3, 4, 5, 6]]
#print (chr_2) #[[1, -3, -6, -5], [2, -4]]

def chromosome_to_cycle(lst):
    cycle = []
    for i in lst:
        if i > 0:
            cycle.append(2*i-1)
            cycle.append(2*i)
        else:
            cycle.append(2*-i)
            cycle.append(2*-i-1)
    return cycle

def colored_edges(chr_lst):
    edges = set()
    for chr in chr_lst:
        cycle = chromosome_to_cycle(chr)
        if chr[0] > 0:
            cycle.append(2*chr[0]-1)
        else:
            cycle.append(2*-chr[0])
        for i in range(len(chr)):
            edges.add(tuple(cycle[2*i+1:2*i+3]))
    edges = list(edges)
    return_edges = []
    for tp in edges:
        return_edges.append(list(tp))
    return return_edges

genome_graph_1 = colored_edges(chr_1)
genome_graph_2 = colored_edges(chr_2)
#print (genome_graph_1)
#print (genome_graph_2)

def graph_generator(graph_1, graph_2):
    graph = {}
    for i in range(block*2):
        graph[i + 1] = []
    for edge in graph_1:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    for edge in graph_2:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

genome_graph = graph_generator(genome_graph_1, genome_graph_2)

def DFS(start_node, visited_bool, cc):
    dfs_stack = deque()
    dfs_stack.append(start_node)
    while dfs_stack:
        v = dfs_stack.pop()
        if visited_bool[v] == False:
            visited_bool[v] = True
            cc.append(v)
            for arr_node in genome_graph[v]:
                dfs_stack.append(arr_node)

visited_bool = [False] * (block*2 + 1)
total_components = []
for i in range(1, block*2+1):
    cc = []
    if visited_bool[i] == False:
        DFS(i, visited_bool, cc)
        total_components.append(cc)

print(block - len(total_components))
