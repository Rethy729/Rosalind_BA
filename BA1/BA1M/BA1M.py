f = open("rosalind_ba1m.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

NtP = {0:'A',1:'C',2:'G',3:'T'}

index = int(data[0])
k = int(data[1])

def Number_to_Pattern(num, k):

    if k == 1:
        return NtP[num]

    mok = num // (4**(k-1))
    namoji = num % (4**(k-1))

    return NtP[mok] + Number_to_Pattern(namoji, k-1)

print (Number_to_Pattern(index, k))
