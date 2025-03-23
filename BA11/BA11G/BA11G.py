import numpy

aa_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
                'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #20

mass_aa = {k: v for v, k in aa_mass.items()}

f = open('rosalind_ba11g.txt', 'r')
data = f.readlines()
def data_processing(data):
    spec_vecs = []
    threshold = int(data[-1])
    peptide = data[-2].strip()
    for line in data[:-2]:
        spec_vecs.append(list(map(int, line.strip().split())))
    return spec_vecs, peptide, threshold

spec_vecs, peptide, threshold = data_processing(data)

def all_sub_peptide(str, spec_vec): #spec_vecs is a list containing n spec_vec
    max_len = -99999999
    min_len = 99999999
    for spec in spec_vec:
        if len(spec) > max_len:
            max_len = len(spec)
        if len(spec) < min_len:
            min_len = len(spec)
    all_sub_peptide = []
    for i in range(min_len//187, max_len//56):
        for j in range(len(str)-i+1):
            sub_string = str[j:j+i]
            all_sub_peptide.append(sub_string)
    return all_sub_peptide

all_sub_peptide = all_sub_peptide(peptide, spec_vecs)

def P_PV(peptide):
    PV = []
    for aa in peptide:
        pv = [0]*(aa_mass[aa]-1)
        pv.append(1)
        PV += pv
    return PV

def score_peptide(peptide_lst, spec_vec, threshold):
    max_score = -99999999
    max_peptide = ''
    for sub in peptide_lst:
        PV = P_PV(sub)
        if len(PV) == len(spec_vec):
            score = numpy.dot(PV, spec_vec)
            if score > max_score:
                max_score = score
                max_peptide = sub
    if max_score >= threshold:
        return max_peptide

answer = []
for spec_vec in spec_vecs:
    peptide_temp = score_peptide(all_sub_peptide, spec_vec, threshold)
    if peptide_temp != None:
        answer.append(peptide_temp)
answer_lst = list(set(answer))
for peptide in answer_lst:
    print (peptide)
