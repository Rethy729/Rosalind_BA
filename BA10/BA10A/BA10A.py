f = open('rosalind_ba10a.txt', 'r')
data = f.readlines()

def data_processing (data):
    path = data[0].strip()
    symbol_1 = list(map(str, data[2].split()))[0]
    symbol_2 = list(map(str, data[2].split()))[1]
    transition_matrix = []
    transition_matrix.append(list(map(float, data[5].strip().split()[1:])))
    transition_matrix.append(list(map(float, data[6].strip().split()[1:])))
    return path, symbol_1, symbol_2, transition_matrix

path, symbol_1, symbol_2, transition_matrix = data_processing(data)

def path_probability(path, symbol_1, symbol_2, transition_matrix):
    probability = 0.5
    prob_dict = {symbol_1+symbol_1:transition_matrix[0][0], symbol_1+symbol_2:transition_matrix[0][1], symbol_2+symbol_1:transition_matrix[1][0], symbol_2+symbol_2:transition_matrix[1][1]}
    for i in range(len(path)-1):
        probability *= prob_dict[path[i:i+2]]
    return probability

print (path_probability(path, symbol_1, symbol_2, transition_matrix))


