protein_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}

f = open("rosalind_ba4c.txt", 'r')
data = f.read()
sequence = data[:-1]

def mass(seq):
    answer = 0
    for aa in seq:
        answer += protein_mass[aa]
    return answer

def mass_spec(seq):
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


print (' '.join(map(str, mass_spec(sequence))))
