f = open("rosalind_ba2h.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

pattern = data[0]
DNA_seq = list(map(str, data[1].split(' ')))

def HammingDistance(seq1, seq2): #len(seq1) == len(seq2)
    HD = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            HD += 1
    return HD

def DBPAS(pattern, DNA_seq):
    k = pattern
    distance = 0
    for string in DNA_seq:
        hd = len(k)
        for i in range(len(string)-len(k)+1):
            if hd > HammingDistance(k, string[i:i+len(k)]):
                hd = HammingDistance(k, string[i:i+len(k)])
        distance += hd
    return distance

print (DBPAS(pattern, DNA_seq))
                            
