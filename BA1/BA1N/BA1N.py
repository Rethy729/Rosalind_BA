f = open("rosalind_ba1n.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

PM = {'A':['C', 'G', 'T'],'C':['A', 'G', 'T'],'G':['A', 'C', 'T'],'T':['A', 'C', 'G']}
genome = list(data[0])
d = int(data[1])

string_set = set()

def point_mutation(pattern, d):
    if d == 0:
        return
    string_set.add(''.join(pattern))
    
    for i in range(len(genome)):
        temp_pattern = pattern[:]
        for pm in PM[pattern[i]]:
            temp_pattern[i] = pm
            string_set.add(''.join(temp_pattern)) 
            point_mutation(temp_pattern, d-1)

point_mutation(genome, d)

w = open("output_ba1n.txt", 'w')

for elements in string_set:
    w.write(elements+'\n')
w.close()
            
