f = open("rosalind_ba4g.txt", 'r')
data = f.readlines()

cut_n = int(data[0])
cyclospectrum = list(map(int, data[1].split(' ')))

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
'''
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
'''
def expand(peptides_set): # working well
    new_set = set()
    for peptide in peptides_set:
        for aa in AminoAcid:
            new_set.add(peptide+aa)
    return new_set

def score(lst1, lst2): #same function with IN_score from BA4F
    temp_lst1 = lst1[:]
    temp_lst2 = lst2[:]
    for num in temp_lst1:
        if num in temp_lst2:
            temp_lst2.remove(num)
    return len(lst2) - len(temp_lst2)

def CUT(input_set, spectrum, n):
    lst = list(input_set)
    lst_data = []
    for peptide in lst:
        lst_data.append([score(circ_mass_spec(peptide), spectrum), peptide])
    lst_data.sort(reverse=True)
    cut_set = set()
    for i in range(n):
        if i>=len(lst_data):
            break
        else:
            cut_set.add(lst_data[i][1])
    return cut_set

def LCS(spectrum, n): #same algorithm with LeaderboardCyclopeptideSequencing
    leaderboard = set()
    leaderboard.add('')

    leader_peptide = ''
    while len(leaderboard)!=0:
        leaderboard = expand(leaderboard)
        bound_set = set()
        for peptide in leaderboard:
            if mass(peptide) == spectrum[-1] and score(circ_mass_spec(peptide), spectrum) > score(circ_mass_spec(leader_peptide), spectrum):
                leader_peptide = peptide
            elif mass(peptide) > spectrum[-1]:
                bound_set.add(peptide)
        leaderboard = (leaderboard-bound_set)
        leaderboard = CUT(leaderboard, spectrum, n)
    return leader_peptide

def printpeptide(peptide):
    aa_mass = []
    for aa in peptide:
        aa_mass.append(protein_mass[aa])
    return aa_mass
'''
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
'''

answer = (printpeptide(LCS(cyclospectrum, cut_n)))
print('-'.join(map(str, answer)))

'''
w = open("output_ba4g.txt", 'w')
for set in answer:
    w.write('-'.join(map(str, set))+' ')
w.close()'''