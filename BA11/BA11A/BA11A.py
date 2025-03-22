protein_mass_old = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'N':114,
                'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #18 (deleted Q, L)
protein_mass = {v: k for k, v in protein_mass_old.items()}

f = open('rosalind_ba11a.txt', 'r')
spectrum = list(map(int, f.readlines()[0].strip().split()))


def build_graph(spec):
    spec = [0] + spec
    spec_graph = []
    for i in range(len(spec)):
        for j in range(i, len(spec)):
            if spec[j] - spec[i] > 186:
                break
            if (spec[j] -spec[i]) in protein_mass:
                spec_graph.append([spec[i], spec[j], protein_mass[spec[j]-spec[i]]])
    return spec_graph

answer = build_graph(spectrum)

w = open('output_ba11a.txt', 'w')
for line in answer:
    w.write(f'{line[0]}->{line[1]}:{line[2]}'+'\n')
w.close()