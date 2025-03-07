f = open("rosalind_ba2e.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

k = (list(map(int, data[0].split(' '))))[0]
d = (list(map(int, data[0].split(' '))))[1]

DNA_seq = []
for i in range(1, len(data)-1):
    DNA_seq.append(data[i])
    
base_index = {'A':0, 'C':1, 'G':2, 'T':3}
base_index_rev = {0:'A', 1:'C', 2:'G', 3:'T'}

def prob_matrix(kmer_matrix): #generates a prob matrix of the input kmer

    frequency = []
    for i in range(k):
        frequency.append([1, 1, 1, 1])

    for kmer in kmer_matrix:
        for i in range(k):
            frequency[i][base_index[kmer[i]]] += 1

    for i in range(len(frequency)): #converting frequency into probability
        for j in range(len(frequency[0])):
            frequency[i][j] = (frequency[i][j]*1.0)/(d+1)
            
    return frequency

def consensus(kmer_matrix): #gets kmer-matrix (But since k is defined already, this function works even though it is not kmer-matrix), generates a consensus
    
    kmer_prob = prob_matrix(kmer_matrix)
    consensus = ''
    for prob in kmer_prob:
        max_prob = max(prob)
        consensus = consensus + base_index_rev[prob.index(max_prob)]
    
    return consensus

def HammingDistance(seq1, seq2): #len(seq1) == len(seq2)
    
    HD = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            HD += 1
    return HD

def score(kmer_matrix): #gets kmer-matrix (This function may not work if the input matrix element is not strictly kmer), returns a score of the matrix
    
    kmer_consensus = consensus(kmer_matrix)
    score = 0
    for kmer in kmer_matrix:
        score += HammingDistance(kmer, kmer_consensus)
        
    return score
  
def find_probable_kmer(sequence, kmer_matrix): #gets kmer-matrix and a long DNA sequence, finding the most-probable kmer in the sequence
    
    prob = prob_matrix(kmer_matrix)
    
    probability = []
    for i in range(len(sequence)-k+1):
        sub_sequence = sequence[i:i+k]
        prob_kmer = 1
        for j in range(len(sub_sequence)):
            prob_kmer = prob_kmer * prob[j][base_index[sub_sequence[j]]]
        probability.append(prob_kmer)
    max_prob = max(probability)
    
    return sequence[probability.index(max_prob):probability.index(max_prob)+k]
            
def GreedyMotifSearch(seq_list): #its structure is identical to the pseudo-code
    
    Bestmotif = []
    
    for seq in seq_list:
        Bestmotif.append(seq[:k])
    Bestscore = score(Bestmotif)

    first_DNA = seq_list[0]
    
    for i in range(len(first_DNA)-k+1):
        motif = []
        motif.append(first_DNA[i:i+k])
        for j in range(1, len(seq_list)):
            motif.append(find_probable_kmer(seq_list[j], motif))
        score_i = score(motif)
        
        if score_i < Bestscore:
            Bestscore = score_i
            Bestmotif = motif
            
    return Bestmotif

answer = GreedyMotifSearch(DNA_seq)
for kmer in answer:
    print (kmer)
