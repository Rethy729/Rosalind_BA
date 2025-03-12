f = open('rosalind_ba6k.txt', 'r')
data = f.readlines()

def data_processing(data):
    chromosome_lst = list(map(str, data[0][1:-2].split(')(')))
    chromosome = []
    for chr in chromosome_lst:
        chromosome_temp = list(map(int, chr.split(' ')))
        chromosome.append(chromosome_temp)
    indices = list(map(int, data[1][:-1].split(', ')))
    return chromosome, indices

chromosome_data, indices_data = data_processing(data)
#print (chromosome_data)

def lsttostr(lst):
    lst_str = []
    for num in lst:
        if num > 0:
            lst_str.append('+'+str(num))
        else:
            lst_str.append(str(num))
    return ('(' + ' '.join(map(str, lst_str)) + ')')

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

def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(1, len(cycle)//2+1):
        if cycle[2*i-2] < cycle[2*i-1]:
            chromosome.append(cycle[2*i-1]//2)
        else:
            chromosome.append(-cycle[2*i-2]//2)
    return lsttostr(chromosome)

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

genome_graph = colored_edges(chromosome_data)
#print(genome_graph)

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

genome_graph_changed = two_break_on_genome_graph(genome_graph, indices_data)
#print (genome_graph_changed)

def next_edge_determine(num):
    if num%2 ==0:
        return num-1
    else:
        return num+1

def graph_to_genome(graph_edges):
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
        cycles.append(temp_cycle)
    #print (cycles)
    cycles_line = []
    for cycle in cycles:
        temp_cyc = []
        for edges in cycle:
            temp_cyc.append(edges[0])
            temp_cyc.append(edges[1])
        temp_cyc_2 = temp_cyc[:-1]
        cycles_line.append([temp_cyc[-1]]+temp_cyc_2)
    #print (cycles_line)
    chromosome = []
    for line in cycles_line:
        chromosome.append(cycle_to_chromosome(line))
    return chromosome

print (graph_to_genome(genome_graph_changed))