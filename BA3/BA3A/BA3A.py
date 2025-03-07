f = open("rosalind_ba3a.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

k = int(data[0])
DNA = data[1]

kmer = set()

for i in range(len(DNA)-k+1):
    kmer.add(DNA[i:i+k])

kmer_list = list(kmer)

w = open("output_ba3a.txt", 'w')
for kmer in kmer_list:
    w.write(kmer+'\n')
w.close()
