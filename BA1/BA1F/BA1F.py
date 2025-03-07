f = open("rosalind_ba1f.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
genome = data[0]

skew = 0
skew_rec = []

for base in genome:
    if base == 'C':
        skew -= 1
    elif base == 'G':
        skew += 1
        
    skew_rec.append(skew)

skew_min = min(skew_rec)
answer = []

for i in range(len(skew_rec)):
    if skew_rec[i] == skew_min:
        answer.append(i+1)

print(' '.join(map(str, answer)))

        
