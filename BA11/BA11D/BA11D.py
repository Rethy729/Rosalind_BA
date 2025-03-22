aa_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
                'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #20

mass_aa = {k: v for v, k in aa_mass.items()}

f = open('rosalind_ba11d.txt', 'r')
spectrum = list(map(int, f.readlines()[0].strip().split()))

def PV_P(lst):
    peptide = ''
    j = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            peptide += mass_aa[(i + 1) - j]
            j = i + 1
    return peptide
print (PV_P(spectrum))

