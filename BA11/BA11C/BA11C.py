aa_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
                'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #20

f = open('rosalind_ba11c.txt', 'r')
peptide = f.readlines()[0].strip()
print (peptide)

def P_PV(peptide):
    PV = []
    for aa in peptide:
        pv = [0]*(aa_mass[aa]-1)
        pv.append(1)
        PV += pv
    return PV

print (' '.join(map(str, P_PV(peptide))))