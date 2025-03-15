f = open('rosalind_ba9p.txt', 'r')
data = f.read().split('-\n')

def data_processing(data):
    data_list = list(map(str, data[0].strip().split('\n')))
    max_node = int(list(map(str, data_list[-1].split(' -> ')))[0])
    node_data = {}
    for data_line in data_list:
        if data_line[-1] != '}':
            data_line_temp = list(map(str, data_line.strip().split(' -> ')))
            node_data[int(data_line_temp[0])] = list(map(int, data_line_temp[1].split(',')))

    color_list = list(map(str, data[1].strip().split('\n')))
    red = []
    blue = []
    for line in color_list:
        if line[-1] == 'd':
            red.append(int(list(map(str, line.split(': ')))[0]))
        else:
            blue.append(int(list(map(str, line.split(': ')))[0]))

    return max_node, node_data, red, blue

max_node, node_data, red, blue = data_processing(data)

def tree_coloring(max_node, node_data, red, blue):
    purple = []
    while len(red)+len(blue)+len(purple) != (max_node+1):
        whole = red+blue+purple
        for node in node_data:
            if node in whole:
                continue

            check = []
            for arr_node in node_data[node]:
                if arr_node in red:
                    check.append(0)
                elif arr_node in blue:
                    check.append(1)
                elif arr_node in purple:
                    check.append(2)
                else:
                    check.append(3)
            if 3 not in check:
                if len(set(check)) == 1:
                    if check[0] == 0:
                        red.append(node)
                    elif check[0] == 1:
                        blue.append(node)
                    elif check[0] == 2:
                        purple.append(node)
                else:
                    purple.append(node)
            else:
                continue

    color_data = []
    for node in red:
        color_data.append([node, 'red'])
    for node in blue:
        color_data.append([node, 'blue'])
    for node in purple:
        color_data.append([node, 'purple'])
    color_data.sort()
    return color_data

answer = (tree_coloring(max_node, node_data, red, blue))
for line in answer:
    print(str(line[0])+': '+line[1])