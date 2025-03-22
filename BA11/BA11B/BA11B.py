from collections import defaultdict
import random

aa_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'N':114,
                'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #18 (deleted Q, L)
mass_aa = {v: k for k, v in aa_mass.items()}

f = open('rosalind_ba11b.txt', 'r')
spectrum = list(map(int, f.readlines()[0].strip().split()))

def build_graph(spec):
    spec = [0] + spec
    spec_graph = defaultdict(dict)

    for i in range(len(spec)):
        for j in range(i, len(spec)):
            if spec[j] - spec[i] > 186:
                break
            if (spec[j] -spec[i]) in mass_aa:
                spec_graph[spec[i]][spec[j]] = mass_aa[spec[j]-spec[i]]
    return spec_graph

spec_graph = build_graph(spectrum)
print (spec_graph)

def check_spec(str):
    spec = []
    total_sum = 0
    for aa in str:
        total_sum += aa_mass[aa]
    spec.append(total_sum)
    for i in range(len(str)-1):
        sub_string_1 = str[:i+1]
        sub_string_2 = str[i+1:]
        str1_mass = 0
        str2_mass = 0
        for aa in sub_string_1:
            str1_mass += aa_mass[aa]
        for aa in sub_string_2:
            str2_mass += aa_mass[aa]
        spec.append(str1_mass)
        spec.append(str2_mass)
    spec.sort()
    return spec

#print (check_spec('GPFNA'))

def find_route(graph, spec):
    while True:
        peptide = ''
        start = random.choice(list(graph[0]))
        peptide += graph[0][start]
        while start in graph:
            next = random.choice(list(graph[start]))
            peptide += graph[start][next]
            start = next
        if check_spec(peptide) == spec:
            return peptide

print(find_route(spec_graph, spectrum))

