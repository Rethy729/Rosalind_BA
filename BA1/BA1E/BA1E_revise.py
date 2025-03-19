from collections import defaultdict

f = open("rosalind_ba1e.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
string = data[0]
index_list = list(map(int, data[1].split(' ')))

k, l, t = index_list[0], index_list[1], index_list[2]

initial_l = string[:l]


kmer_index_dict = defaultdict(list)
for i in range(l-k+1):
    kmer_index_dict[initial_l[i:i + k]].append(i)

#print (kmer_index_dict)

answer = set()
for i in range(1, len(string)-l+1):
    kmer_index_dict[string[i-1 : i-1+k]].remove(i-1)
    kmer_index_dict[string[(l-1)+i-k : (l-1)+i]].append((l-1)+i-k)
    for key in kmer_index_dict:
        if len(kmer_index_dict[key]) >= t:
            answer.add(key)

answer_list = list(answer)

print(' '.join(map(str, answer_list)))

#O(linear)