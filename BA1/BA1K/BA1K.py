f = open("rosalind_ba1k.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

template = data[0]
k = int(data[1])

def kmer_creation(k):
    if k == 1:
        return ['A', 'C', 'G', 'T']
    kmer = []
    for mer in kmer_creation(k-1):
        for base in kmer_creation(1):
            kmer.append(mer+base)
    return kmer

frequency = []
for kmer in kmer_creation(k):
    kmer_frequency = 0
    for i in range(len(template)-k+1):
        if kmer == template[i:i+k]:
            kmer_frequency += 1
    frequency.append(kmer_frequency)

w = open('output_ba1k.txt', 'w')
write = w.write(' '.join(map(str, frequency)))
w.close()
