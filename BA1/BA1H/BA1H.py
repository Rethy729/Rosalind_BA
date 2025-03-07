f = open("rosalind_ba1h.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

string = data[0]
def HammingDistance(start_index, string): #finds the HD starting from the start_index of template
    HD = 0
    for i in range(start_index, start_index+len(string)):
        if template[i] != string[i - start_index]:
            HD += 1
    return HD

template = data[1]
upper_bound = int(data[2])
answer = []

for i in range(0, len(template)-len(string)+1):
    if upper_bound>=HammingDistance(i, string):
        answer.append(i)

print(' '.join(map(str, answer)))
