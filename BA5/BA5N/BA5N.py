import queue

f = open('rosalind_ba5n.txt', 'r')
data = f.readlines()

def graphtodict(data):
    graph = {}
    for line in data:
        line_s = list(map(str, line.strip().split(' -> ')))
        graph[int(line_s[0])] = []
        arr_node_lst = list(map(int, line_s[1].split(',')))
        for arr_node in arr_node_lst:
            graph[int(line_s[0])].append(arr_node)
    return graph

DAG = graphtodict(data)
#print (DAG)

def incoming_degree_count(graphdata):
    node_set = set()
    for key in graphdata:
        node_set.add(key)
        for node in graphdata[key]:
            node_set.add(node)
    node_lst = list(node_set)
    IDC = [0] * (max(node_lst)+1)
    for key in graphdata:
        for arr_node in graphdata[key]:
            IDC[arr_node] += 1
    return IDC

IDC = incoming_degree_count(DAG)
#print (incoming_degree_count(DAG))

def khan(idc_lst, graphdata):
    dag_queue = queue.Queue()

    for i in range(len(idc_lst)): #appending the first idc == 0 nodes in dag_queue
        if idc_lst[i] == 0:
            dag_queue.put(i)

    topo_sort = []
    while len(topo_sort) != len(idc_lst): #next, until we get all the nodes in topo_sort
        node = dag_queue.get()
        topo_sort.append(node)
        if node in graphdata:
            for arr_node in graphdata[node]:
                idc_lst[arr_node] -= 1
                if idc_lst[arr_node] == 0:
                    dag_queue.put(arr_node)
        else:
            continue
    return topo_sort

print (khan(IDC, DAG))



