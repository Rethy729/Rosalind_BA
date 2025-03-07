f = open("rosalind_ba1i.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

template = data[0]
k = (list(map(int, data[1].split(' '))))[0]
d = (list(map(int, data[1].split(' '))))[1]

def kmer_creation(k):
    if k == 1:
        return ['A', 'C', 'G', 'T']
    kmer = []
    for mer in kmer_creation(k-1):
        for base in kmer_creation(1):
            kmer.append(base+mer)
    return kmer

def HammingDistance(start_index, string): #finds the HD starting from the start_index of template
    HD = 0
    for i in range(start_index, start_index+len(string)):
        if template[i] != string[i - start_index]:
            HD += 1
    return HD

def frequent_test(kmer_list, template, upper_HD):
    
    frequency = []
    for kmer in kmer_list:
        kmer_frequency = 0
        for i in range(len(template)-k+1):
            
            if HammingDistance(i, kmer) <= upper_HD:
                kmer_frequency += 1
        frequency.append(kmer_frequency)
        
    max_frequency = max(frequency)
    most_frequent_kmer = []

    for i in range(len(frequency)):
        if frequency[i] == max_frequency:
            most_frequent_kmer.append(kmer_list[i])

    return most_frequent_kmer

kmer_list = kmer_creation(k)
answer = frequent_test(kmer_list, template, d)

print (' '.join(map(str, answer)))
        
