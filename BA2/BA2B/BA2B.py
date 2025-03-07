f = open("rosalind_ba2b.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

def kmer_creation(k):
    if k == 1:
        return ['A', 'C', 'G', 'T']
    kmer = []
    for mer in kmer_creation(k-1):
        for base in kmer_creation(1):
            kmer.append(base+mer)
    return kmer

def HammingDistance(start_index, string, template): #finds the HD starting from the start_index of template
    HD = 0
    for i in range(start_index, start_index+len(string)):
        if template[i] != string[i - start_index]:
            HD += 1
    return HD

k = int(data[0])
DNA_seq = []

for i in range(1, len(data)-1):
    DNA_seq.append(data[i])

kmer_list = kmer_creation(k)

d_kmer = []
for kmer in kmer_list:
    d_sum = 0
    for seq in DNA_seq:
        min_HD = k
        for i in range(len(seq)-k+1):
            if HammingDistance(i, kmer, seq) < min_HD:
                min_HD = HammingDistance(i, kmer, seq)
        d_sum += min_HD
    d_kmer.append([d_sum, kmer])
    
minimum_d = len(DNA_seq)*k 
for pair in d_kmer:
    if pair[0] < minimum_d:
        minimum_d = pair[0]

for pair in d_kmer:
    if pair[0] == minimum_d:
        print (pair[1])
