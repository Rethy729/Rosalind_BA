f = open("rosalind_ba1d.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
pattern = data[0]
genome = data[1]

index = []
for i in range(len(genome)-len(pattern)):
    if genome[i:i+len(pattern)] == pattern:
        index.append(i)

w = open("output_ba1d.txt", 'w')
w.write(' '.join(map(str, index)))
w.close()
