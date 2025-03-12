f = open('rosalind_ba6h.txt', 'r')
data = f.readlines()

def data_processing(data):
    chromosome_lst = list(map(str, data[0][1:-2].split(')(')))
    chromosome = []
    for chr in chromosome_lst:
        chromosome_temp = list(map(int, chr.split(' ')))
        chromosome.append(chromosome_temp)
    return chromosome

chr_lst = data_processing(data)
print (chr_lst)

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
    print (edges)

colored_edges(chr_lst)