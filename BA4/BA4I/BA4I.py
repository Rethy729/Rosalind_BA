#THis code modifies BA4G to work with tuples filled with aa mass e.g) 'GA' -> (57, 71)

f = open("rosalind_ba4i.txt", 'r')
data = f.readlines()
convolution_n = int(data[0])
cut_n = int(data[1])
cyclospectrum = list(map(int, data[2].split(' ')))

#protein_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'L':113, 'N':114, 'D':115, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #exiled I(113), K(128)
#AminoAcid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']

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

def sort(lst, m):
    multi = {}
    for num in lst:
        if num in multi:
            multi[num] += 1
        else:
            multi[num] = 1
    multi_sorted = sorted(multi.items(), key = lambda item:item[1], reverse=True)
    aa = []

    temp_m = 0
    for key in multi_sorted:
        if key[0]>=57 and key[0]<=200:
            aa.append(key[0])
            temp_m += 1

        if temp_m == m:
            break
    return aa

aa_mass = sort(convolution(cyclospectrum), convolution_n)

def mass(peptide): #working well
    tm = 0
    for aa in peptide:
        tm += aa
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

def expand(peptides_set): # working well
    new_set = set()
    for peptide in peptides_set:
        for aa in aa_mass:
            aa_tuple = (aa,)
            new_set.add(peptide+aa_tuple)
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
    empty_tuple = ()
    leaderboard.add(empty_tuple)

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

answer = (LCS(cyclospectrum, cut_n))
'''
def printpeptide(peptide):
    aa_mass = []
    for aa in peptide:
        aa_mass.append(protein_mass[aa])
    return aa_mass
'''
print('-'.join(map(str, answer)))
