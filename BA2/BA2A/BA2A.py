f = open("rosalind_ba2a.txt", 'r')
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

k = list(map(int, data[0].split(' ')))[0]
d = list(map(int, data[0].split(' ')))[1]

DNA_seq = []
for i in range(1, len(data)-1):
    DNA_seq.append(data[i])

kmer_cand = kmer_creation(k)
kmer_collection = []
for kmer in kmer_cand:
    count = 0 # count==len(DNA_seq) means kmer has a position in every seq which has HD <= d
    for seq in DNA_seq:
        match_count = 0 # match count != 0 means kmer has a position in seq which has HD <= d
        for i in range(len(seq)-k+1):
            if HammingDistance(i, kmer, seq) <= d:
                match_count += 1
        if match_count != 0:
            count += 1
    if count == len(DNA_seq):
        kmer_collection.append(kmer)
                
w = open('output_ba2a.txt', 'w')
w.write(' '.join(map(str, kmer_collection)))
w.close()
