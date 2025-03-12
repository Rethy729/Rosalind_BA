f = open('rosalind_ba6e.txt', 'r')
data = f.readlines()

def dataprocessing(data):
    k = int(data[0])
    str1 = data[1].strip()
    str2 = data[2].strip()
    return k, str1, str2

def reversecomp(str):
    comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev = ''
    for base in str:
        rev = comp[base] + rev
    return rev

k, str1, str2 = dataprocessing(data)

def dictgen(str, k):
    kmer_dict = {}
    for i in range(len(str)-k+1):
        kmer_tuple = (str[i:i+k], reversecomp(str[i:i+k]))
        if kmer_tuple in kmer_dict:
            kmer_dict[kmer_tuple].append(i)
        else:
            kmer_dict[kmer_tuple] = [i]
    return kmer_dict

kmer_dict = dictgen(str1, k)

def comparing(kmer_dict, string):
    for i in range(len(string)-k+1):
        kmer = (string[i:i+k], reversecomp(string[i:i+k]))
        kmer_2 = (reversecomp(string[i:i+k]), string[i:i+k])
        if kmer in kmer_dict:
            for idx in kmer_dict[kmer]:
                print('('+str(idx)+', '+str(i)+')')
        elif kmer_2 in kmer_dict:
            for idx in kmer_dict[kmer_2]:
                print('('+ str(idx) +', '+ str(i) +')')

comparing(kmer_dict, str2)



