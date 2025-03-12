f = open('rosalind_ba6j.txt', 'r')
data = f.readlines()
print (data)
def data_processing(data):
    edge_lst = list(map(str, data[0][1:-2].split('), (')))
    edges = []
    for edge in edge_lst:
        edges.append(list(map(int, edge.split(', '))))
    indices  = list(map(int, data[1][:-1].split(', ')))
    return edges, indices

edge_data, indices_data = data_processing(data)

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

answer = two_break_on_genome_graph(edge_data, indices_data)
for i in range(len(answer)):
    answer[i] = tuple(answer[i])
print(', '.join(map(str, answer)))
