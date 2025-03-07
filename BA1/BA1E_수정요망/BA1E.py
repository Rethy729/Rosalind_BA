# I think this code can be faster

f = open("rosalind_ba1e.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
string = data[0]
index_list = list(map(int, data[1].split(' ')))

k, l, t = index_list[0], index_list[1], index_list[2]

answer = set()

for i in range(len(string)-l+1):
    kmer_index_temp = {}
    for j in range(i, i+l-k+1):
        if string[j:j+k] in kmer_index_temp:
            kmer_index_temp[string[j:j+k]].append(j)
        else:
            kmer_index_temp[string[j:j+k]] = [j]
    for key in kmer_index_temp:
        if len(kmer_index_temp[key]) >= t:
            answer.add(key)

answer_list = list(answer)

print(' '.join(map(str, answer_list)))
