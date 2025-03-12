f = open('rosalind_ba6i.txt', 'r')
data = f.readlines()
#print (data)
def data_processing(data):
    edge_lst = list(map(str, data[0][1:-2].split('), (')))
    edges = []
    for edge in edge_lst:
        edges.append(list(map(int, edge.split(', '))))
    return edges

genome_graph = data_processing(data) #[[2, 3], [4, 5] ....]
#print(genome_graph)

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

print (''.join(map(str, graph_to_genome(genome_graph))))