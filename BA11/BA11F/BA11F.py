import numpy

aa_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
                'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #20

mass_aa = {k: v for v, k in aa_mass.items()}

f = open('rosalind_ba11f.txt', 'r')
data = f.readlines()
spectral_vector = list(map(int, data[0].strip().split()))
peptide = data[1].strip()

def all_sub_peptide(str, spec_vec):
    spec_vec_len = len(spec_vec)
    all_sub_peptide = []
    for i in range(len(spec_vec)//187, len(spec_vec)//56):
        for j in range(len(str)-i+1):
            sub_string = str[j:j+i]
            all_sub_peptide.append(str[j:j+i])
    return all_sub_peptide

all_sub_peptide = all_sub_peptide(peptide, spectral_vector)
#print (all_sub_peptide)

def P_PV(peptide):
    PV = []
    for aa in peptide:
        pv = [0]*(aa_mass[aa]-1)
        pv.append(1)
        PV += pv
    return PV

def max_score_peptide(peptide_lst, spec_vec):
    max_score = -99999999
    max_peptide = ''
    for sub in peptide_lst:
        PV = P_PV(sub)
        #print (len(PV), len(spec_vec))
        if len(PV) == len(spec_vec):
            score = numpy.dot(PV, spec_vec)
            if score > max_score:
                max_score = score
                max_peptide = sub
    return max_peptide

print (max_score_peptide(all_sub_peptide, spectral_vector))