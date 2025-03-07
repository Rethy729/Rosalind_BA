f = open("rosalind_ba1b.txt", 'r')
data = f.read()
data_split = data.split('\n')
string = data_split[0]
k = int(data_split[1])

frequency = {}
for i in range(len(string)-k):
    if string[i:i+k] in frequency:
        frequency[string[i:i+k]] +=1
    else:
        frequency[string[i:i+k]] = 1
        
max_frequency = 0
for key in frequency:
    if max_frequency < frequency[key]:
        max_frequency = frequency[key]

answer = []
for key in frequency:
    if frequency[key] == max_frequency:
        answer.append(key)

print(' '.join(map(str, answer)))
