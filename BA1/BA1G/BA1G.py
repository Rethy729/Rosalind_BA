f = open("rosalind_ba1g.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
genome_1 = data[0]
genome_2 = data[1]

HD = 0

for i in range(len(genome_1)):
    if genome_1[i] != genome_2[i]:
        HD += 1

print (HD)
