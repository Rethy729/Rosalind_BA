import random

f = open("rosalind_ba2g.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
k = (list(map(int, data[0].split(' '))))[0]
d = (list(map(int, data[0].split(' '))))[1]
N = (list(map(int, data[0].split(' '))))[2]
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
  
def find_probable_kmer_random(sequence, kmer_matrix): #gets kmer-matrix and a long DNA sequence, finding the most-probable kmer in the sequence
    prob = prob_matrix(kmer_matrix)
    
    probability = []
    for i in range(len(sequence)-k+1):
        sub_sequence = sequence[i:i+k]
        prob_kmer = 1
        for j in range(len(sub_sequence)):
            prob_kmer = prob_kmer * prob[j][base_index[sub_sequence[j]]]
        probability.append(prob_kmer)

    index = []
    prob_sum = sum(probability)
    for i in range(len(probability)):
        index.append(i)
        probability[i] = probability[i]/prob_sum
    skewed_index = random.choices(index, weights = probability, k=1)[0]
    return sequence[skewed_index:skewed_index+k]

def GibbsSampler(seq_list): #its structure is identical to the pseudo-code
    
    Bestmotif = []
    for seq in seq_list:
        random_index = random.randint(0, len(seq_list[0])-k) 
        Bestmotif.append(seq[random_index:random_index+k])
    Bestscore = score(Bestmotif)

    for i in range(N):
        motif = [0]*d
        j = random.randint(0, d-1) #choose among 0, 1, 2, 3, 4
        for m in range(len(Bestmotif)):
            if j == m:
                continue
            motif[m] = Bestmotif[m]
        motif[j] = (find_probable_kmer_random(seq_list[j], motif[:j]+motif[j+1:]))
        score_i = score(motif)
        if score_i < Bestscore:
            Bestscore = score_i
            Bestmotif = motif
    return Bestmotif

BestofBest_motif = GibbsSampler(DNA_seq)
BestofBest_score = score(BestofBest_motif)

for i in range(30):
    temp_motif = GibbsSampler(DNA_seq)
    if score(temp_motif) < BestofBest_score:
        BestofBest_motif = temp_motif
        BestofBest_score = score(temp_motif)

for kmer in BestofBest_motif:
    print (kmer)

