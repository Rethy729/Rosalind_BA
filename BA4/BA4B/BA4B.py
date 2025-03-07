amino_acid = {('TAA', 'TAG', 'TGA'): 'X', ('TTT', 'TTC'):'F', ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'):'L', ('ATT', 'ATC', 'ATA'):'I', ('ATG'):'M', ('GTT', 'GTC', 'GTA', 'GTG'):'V', ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'):'S',('CCT', 'CCC', 'CCA', 'CCG'):'P', ('ACT', 'ACC', 'ACA', 'ACG'):'T', ('GCT', 'GCC', 'GCA', 'GCG'):'A', ('TAT', 'TAC'):'Y', ('CAT', 'CAC'):'H', ('CAA', 'CAG'):'Q', ('AAT', 'AAC'):'N', ('AAA', 'AAG'):'K', ('GAT', 'GAC'):'D', ('GAA', 'GAG'):'E',('TGT', 'TGC'):'C', ('TGG'):'W', ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'):'R', ('GGT', 'GGC', 'GGA', 'GGG'):'G'}

def complement(strand):
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    complement = '' #3` -> 5`
    for base in strand:
        complement += comp[base]

    comp_strand = complement[::-1] #5` -> 3`
    return comp_strand #returns reverse complement in 5` -> 3`

def ORF_generation(strand):
    strand_set = [strand, complement(strand)]
    frame_set = []
    for template in strand_set:
        for i in range(3): # i = 0, 1, 2
            frame = []
            for j in range(i, len(template)-2, 3):
                codon = template[j:j+3]
                frame.append(codon)
            frame_set.append(frame)
    return frame_set

def translation_matching(frame_set, peptide):
    d = len(peptide)
    substring = []
    for frame in frame_set[:3]: # first 3 elements of frame_set (= original template)
        protein = ''
        for i in range(len(frame)):
            for key in amino_acid:
                if frame[i] in key:
                    protein += amino_acid[key]
        
        for i in range(len(protein)-d+1):
            if protein[i:i+d] == peptide:
                substring.append(frame[i:i+d])

    for frame in frame_set[3:]: # last 3 elements of frame_set (= reverse template)
        protein = ''
        for i in range(len(frame)):
            for key in amino_acid:
                if frame[i] in key:
                    protein += amino_acid[key]

        for i in range(len(protein)-d+1):
            if protein[i:i+d] == peptide:
                comp_substring = []
                frame_rev = frame[i:i+d][::-1]
                for codon in frame_rev:
                    comp_substring.append(complement(codon))  
                substring.append(comp_substring)
    return substring
                    
f = open("rosalind_ba4b.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
template = data[0]
peptide = data[1]

frame_set_1 = ORF_generation(template)
answer = (translation_matching(frame_set_1, peptide))
for line in answer:
    print (''.join(line))