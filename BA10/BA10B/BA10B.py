f = open('rosalind_ba10b.txt', 'r')
data = f.readlines()

def data_processing (data):
    string = data[0].strip()
    path = data[4].strip()
    oc_1 = list(map(str, data[2].split()))[0]
    oc_2 = list(map(str, data[2].split()))[1]
    oc_3 = list(map(str, data[2].split()))[2]
    s_1 = list(map(str, data[6].split()))[0]
    s_2 = list(map(str, data[6].split()))[1]
    emission_1 = list(map(float, data[9].strip().split()[1:]))
    emission_2 = list(map(float, data[10].strip().split()[1:]))
    emission_dict = {s_1+oc_1:emission_1[0], s_1+oc_2:emission_1[1], s_1+oc_3:emission_1[2], s_2+oc_1:emission_2[0], s_2+oc_2:emission_2[1], s_2+oc_3:emission_2[2]}
    return string, path, emission_dict

string, path, emission_dict = data_processing(data)

def emission_probability(string, path, emission_dict):
    probability = 1
    for i in range(len(path)):
        probability *= emission_dict[path[i]+string[i]]
    return probability

print (emission_probability(string, path, emission_dict))
