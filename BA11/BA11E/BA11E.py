from collections import defaultdict
import random
import numpy

aa_mass = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'N':114,
                'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186} #18 (deleted Q, L)
mass_aa = {v: k for k, v in aa_mass.items()}

f = open('rosalind_ba11e.txt', 'r')
spectral_vector = list(map(int, f.readlines()[0].strip().split()))

#print (spectral_vector)
#print (len(spectral_vector))

def build_graph(spec_vec):
    spec_vec = [0] + spec_vec
    spec_graph = defaultdict(dict)

    for i in range(len(spec_vec)-57):
        for j in range(i+57, len(spec_vec)):
            if (j-i) in mass_aa:
                spec_graph[i][j] = mass_aa[j-i]
    return spec_graph

spec_graph = build_graph(spectral_vector)
#print (spec_graph)

def P_PV(peptide):
    PV = []
    for aa in peptide:
        pv = [0]*(aa_mass[aa]-1)
        pv.append(1)
        PV += pv
    return PV

def find_route(graph, start, end, route = []):
    route = route + [start]
    if start == end:
        return [route]
    if start not in graph:
        return []
    routes = []
    for node in graph[start]:
        if node not in route:
            new_routes = find_route(graph, node, end, route)
            for new_route in new_routes:
                routes.append(new_route)
    return routes

def find_peptide (routes, spec_vec):
    max_score = -99999999
    max_route = []
    for route in routes:
        score = 0
        for idx in route[1:]:
            score += spec_vec[idx-1]
        if score > max_score:
            max_score = score
            max_route = route

    peptide = ''
    for i in range(1, len(max_route)):
        peptide += mass_aa[max_route[i] - max_route[i - 1]]

    return peptide

routes = (find_route(spec_graph, 0, len(spectral_vector), route = []))
print (find_peptide(routes, spectral_vector))