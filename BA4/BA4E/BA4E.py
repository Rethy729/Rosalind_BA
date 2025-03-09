f = open("rosalind_ba4e.txt", 'r')
data = f.read()
cyclospectrum = list(map(int, data.split(' ')))
protein_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'L':113, 'N':114, 'D':115, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #exiled I(113), K(128)
AminoAcid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

def mass(peptide): #working well
    tm = 0
    for aa in peptide:
        tm += protein_mass[aa]
    return tm

def circ_mass_spec(seq): #working well
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

def lin_mass_spec(seq): #working well
    sub_seq = []
    for i in range(len(seq)):
        for j in range(i+1):
            sub_seq.append(seq[j:j+len(seq)-i])

    sub_mass = [0]
    for subseq in sub_seq:
        sub_mass.append(mass(subseq))
    sub_mass.sort()
    return sub_mass

def IN(lst1, lst2):#working well, does the same function as: (lst1 in lst2)
    temp_lst1 = lst1[:]
    temp_lst2 = lst2[:]

    for num in temp_lst1:
        if num in temp_lst2:
            temp_lst2.remove(num)
    if (len(lst2) - len(temp_lst2)) == len(lst1):
        return True
    else:
        return False

def expand(peptides_set): # working well
    new_set = set()
    for peptide in peptides_set:
        for aa in AminoAcid:
            new_set.add(peptide+aa)
    return new_set

def CPS(spectrum): #same algorithm with CYCLOPEPTIDESEQUENCING
    peptides = set()
    peptides.add('')

    while len(peptides)!=0:
        peptides = expand(peptides)
        bound_set = set()
        for peptide in peptides:
            lin = lin_mass_spec(peptide)
            if mass(peptide) == spectrum[-1] and circ_mass_spec(peptide) == spectrum:
                return peptide
            elif IN(lin, spectrum) == False:
                bound_set.add(peptide)
        peptides = (peptides-bound_set)

def printeverypeptide(peptide): #peptide with the same cyclosequence = round + reverse and round

    total_peptide = []
    peptide_rev = peptide[::-1]
    peptide_2 = peptide*2
    peptide_rev_2 = peptide_rev*2
    for i in range(len(peptide)):
        total_peptide.append(peptide_2[i:i+len(peptide)])
        total_peptide.append(peptide_rev_2[i:i+len(peptide)])

    aa_mass = []
    for peptide in total_peptide:
        temp_aa = []
        for aa in peptide:
            temp_aa.append(protein_mass[aa])
        aa_mass.append(temp_aa)

    return aa_mass

answer = (printeverypeptide(CPS(cyclospectrum)))
w = open("output_ba4e.txt", 'w')
for set in answer:
    w.write('-'.join(map(str, set))+' ')
w.close()



