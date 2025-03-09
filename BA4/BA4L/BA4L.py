protein_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}

f = open('rosalind_ba4l.txt', 'r')
data = f.readlines()
input_peptide = list(map(str, data[0].split(' ')))
spectrum = list(map(int, data[1].split(' ')))
cut_n = int(data[2])

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

def score(lst1, lst2):
    temp_lst1 = lst1[:]
    temp_lst2 = lst2[:]

    for num in temp_lst1:
        if num in temp_lst2:
            temp_lst2.remove(num)

    return len(lst2) - len(temp_lst2)

def CUT(input_lst, spectrum, n):
    lst_data = []
    for peptide in input_lst:
        lst_data.append([score(LS(peptide), spectrum), peptide])
    lst_data.sort(reverse=True)
    cut_lst = []
    for i in range(n):
        if i>=len(lst_data):
            break
        else:
            cut_lst.append(lst_data[i][1])
    return cut_lst

print (' '.join(map(str, CUT(input_peptide, spectrum, cut_n))))
