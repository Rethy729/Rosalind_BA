from collections import deque

f = open('rosalind_ba6d.txt', 'r')
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

def lsttostr(lst):
    lst_str = []
    for num in lst:
        if num > 0:
            lst_str.append('+'+str(num))
        else:
            lst_str.append(str(num))
    return ('(' + ' '.join(map(str, lst_str)) + ')')

def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(1, len(cycle)//2+1):
        if cycle[2*i-2] < cycle[2*i-1]:
            chromosome.append(cycle[2*i-1]//2)
        else:
            chromosome.append(-cycle[2*i-2]//2)
    return lsttostr(chromosome)

def chromosome_to_cycle(lst):
    cycle = []
    for i in lst:
        if i > 0:
            cycle.append(2*i-1)
            cycle.append(2*i)
        else:
            cycle.append(2*-i)
            cycle.append(2*-i-1)

    return cycle #[1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
    edge_lst = list(edges)
    for i in range(len(edge_lst)):
        edge_lst[i] = list(edge_lst[i])
    return edge_lst #[[2, 3], [4, 5]....]

def output(lst):
    output_str = ''
    for line in lst:
        lst_str = []
        for num in line:
            if num > 0:
                lst_str.append('+'+str(num))
            else:
                lst_str.append(str(num))
        output_str += ('(' + ' '.join(map(str, lst_str)) + ')')
    return output_str #(+1 -2 -3 +4...))

#print(output(chr_1))

def two_break_on_genome_graph(genomegraph, indices_lst):
    i = indices_lst[0]
    i_p = indices_lst[1]
    j = indices_lst[2]
    j_p = indices_lst[3]
    #so, delete (i, i_p) and (j, j_p), add (i, j) and (i_p, j_p). if (i_p, i) is deleted, add (j, i) which is inverted. vice versa
    for n in range(len(genomegraph)):
        if genomegraph[n] == [i, i_p]:
            genomegraph[n] = [i, j]
        elif genomegraph[n] == [i_p, i]:
            genomegraph[n] = [j, i]
        elif genomegraph[n] == [j, j_p]:
            genomegraph[n] = [i_p, j_p]
        elif genomegraph[n] == [j_p, j]:
            genomegraph[n] = [j_p, i_p]
    return genomegraph

def next_edge_determine(num):
    if num%2 ==0:
        return num-1
    else:
        return num+1

def graph_to_genome(graph_edges):
    graph_edge_copy = graph_edges[:]
    cycles = []
    while len(graph_edges) != 0:
        temp_cycle = []
        temp_cycle.append(graph_edges[0])
        graph_edges.remove(graph_edges[0])

        break_bool = True
        while break_bool:
            break_bool = False
            graph_edge_rep = graph_edges[:]
            for edge in graph_edge_rep:
                if next_edge_determine(temp_cycle[-1][1]) == edge[0]:
                    break_bool = True
                    temp_cycle.append(edge)
                    graph_edges.remove(edge)
                elif next_edge_determine(temp_cycle[-1][1]) == edge[1]:
                    break_bool = True
                    temp_cycle.append(edge[::-1])
                    graph_edges.remove(edge)
        #print(temp_cycle)
        cycles.append(temp_cycle)

    #print(cycles)
    cycles_line = []
    for cycle in cycles:
        temp_cyc = []
        for edges in cycle:
            temp_cyc.append(edges[0])
            temp_cyc.append(edges[1])
        temp_cyc_2 = temp_cyc[:-1]
        cycles_line.append([temp_cyc[-1]] + temp_cyc_2)
    #print(cycles_line)
    chromosome = []

    for line in cycles_line:
        chromosome.append(cycle_to_chromosome(line))
    return chromosome, graph_edge_copy

def SRS(chr_1, chr_2):

    def graph_generator(graph_1, graph_2):
        graph = {}
        for i in range(block * 2):
            graph[i + 1] = []
        for edge in graph_1:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        for edge in graph_2:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        for key in graph:
            if len(set(graph[key])) == 1:
                graph[key] = list(set(graph[key]))
        return graph

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

    print (output(chr_1))
    P_edges = colored_edges(chr_1)
    Q_edges = colored_edges(chr_2)
    genome_graph = graph_generator(P_edges, Q_edges)

    visited_bool = [False] * (block * 2 + 1)
    total_components = []
    for i in range(1, block * 2 + 1):
        cc = []
        if visited_bool[i] == False:
            DFS(i, visited_bool, cc)
            total_components.append(cc)

    #print (genome_graph)
    #print (P_edges)
    #print (Q_edges)
    #print(block)

    while len(total_components) != block:
        #print('in')
        #print (P_edges)
        #print (Q_edges)
        #print (genome_graph)
        for edge in Q_edges:
            if len(genome_graph[edge[0]])==2 and len(genome_graph[edge[1]])==2:
                j, i_p = (edge[0], edge[1])
                break
        #for j, i_p
        #print (j, i_p)
        for edge in P_edges:
            if edge[0] == j:
                i = edge[1]
                break
            elif edge[1] == j:
                i = edge[0]
                break
                #(i, j) or (j, i) in P

        for edge in P_edges:
            if edge[0] == i_p:
                j_p = edge[1]
                break
            elif edge[1] == i_p:
                j_p = edge[0]
                break
                #(i_p, j_p) or (j_p, i_p) in P

        #remove (i, j) and (i_p, j_p) from P, add (j, i_p) and (j_p, i) -> (i, j, j_p, i_p)
        #if [i, j] in P_edges and [i_p, j_p] in Q_edges:
        indices_lst = [i, j, j_p, i_p]
        #print (indices_lst)
        P_edges = (two_break_on_genome_graph(P_edges, indices_lst))
        genome_graph = graph_generator(P_edges, Q_edges)
        #print(graph_generator(P_edges, Q_edges))
        genome, P_edges_backup = graph_to_genome(P_edges)
        print (''.join(map(str, genome)))
        P_edges = P_edges_backup

        visited_bool = [False] * (block * 2 + 1)
        total_components = []
        for i in range(1, block * 2 + 1):
            cc = []
            if visited_bool[i] == False:
                DFS(i, visited_bool, cc)
                total_components.append(cc)
        #print(len(total_components))
    #print (P_edges)
    #print (Q_edges)
    #print(output(chr_2))

SRS(chr_1, chr_2)

