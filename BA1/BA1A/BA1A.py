f = open("rosalind_ba1a.txt", 'r')
data = f.read()
data_split = data.split('\n')
n = len(data_split[1])

index = []

for i in range(len(data_split[0])):
    if data_split[0][i:i+n] == data_split[1]:
        index.append(i)

print (len(index))
