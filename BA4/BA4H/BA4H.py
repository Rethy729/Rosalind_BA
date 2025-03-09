f = open("rosalind_ba4h.txt", 'r')
data = f.readlines()
spectrum = list(map(int, data[0].split(' ')))
spectrum.sort()

def convolution(spectrum):
    l = len(spectrum)
    sub = []
    for i in range(l):
        for j in range(i):
            if spectrum[i] == spectrum[j]: #zero SHOULD NOT be in the convolution matrix
                continue
            else:
                sub.append(spectrum[i]-spectrum[j])
    return sub

def sort(lst):
    multi = {}
    for num in lst:
        if num in multi:
            multi[num] += 1
        else:
            multi[num] = 1
    multi_sorted = sorted(multi.items(), key = lambda item:item[1], reverse=True)
    answer = []
    for pair in multi_sorted:
        for i in range(pair[1]):
            answer.append(pair[0])
    return answer


w = open("output_ba4h.txt", 'w')
w.write(' '.join(map(str, sort(convolution(spectrum)))))
w.close()
