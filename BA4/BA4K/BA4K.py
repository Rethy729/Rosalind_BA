protein_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}

f = open('rosalind_ba4k.txt', 'r')
data = f.readlines()
input_peptide = data[0]
spectrum = list(map(int, data[1].split(' ')))

def mass(peptide): #working well
    tm = 0
    for aa in peptide:
        tm += protein_mass[aa]
    return tm

def LS(peptide):
    prefix_mass = [0]
    for i in range(1, len(peptide)):
        prefix_mass.append(mass(peptide[:i]))

    linear_spec = [0]
    for i in range(len(prefix_mass)-1):
        for j in range(i+1, len(prefix_mass)):
            linear_spec.append(prefix_mass[j]-prefix_mass[i])
    linear_spec.sort()
    return linear_spec

def IN_score(lst1, lst2):
    temp_lst1 = lst1[:]
    temp_lst2 = lst2[:]

    for num in temp_lst1:
        if num in temp_lst2:
            temp_lst2.remove(num)

    return len(lst2) - len(temp_lst2)

print(IN_score(LS(input_peptide), spectrum))