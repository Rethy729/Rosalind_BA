protein_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #20

f = open('rosalind_ba4f.txt', 'r')
data = f.readlines()
peptide = data[0][:-1]
spectrum = list(map(int, data[1].split(' ')))

def mass(seq):
    answer = 0
    for aa in seq:
        answer += protein_mass[aa]
    return answer

def circ_mass_spec(seq):
    sub_seq = []
    new_seq = seq * 2
    for i in range(1, len(seq)):
        for j in range(len(seq)):
            sub_seq.append(new_seq[j:j+i])
    sub_seq.append(seq)

    sub_mass = [0]
    for subseq in sub_seq:
        sub_mass.append(mass(subseq))
    sub_mass.sort()
    return sub_mass

def IN_score(lst1, lst2):
    temp_lst1 = lst1[:]
    temp_lst2 = lst2[:]

    for num in temp_lst1:
        if num in temp_lst2:
            temp_lst2.remove(num)

    return len(lst2) - len(temp_lst2)

print (IN_score(circ_mass_spec(peptide), spectrum))