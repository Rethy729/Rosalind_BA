amino_acid = {('TAA', 'TAG', 'TGA'): 'X', ('TTT', 'TTC'):'F', ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'):'L', ('ATT', 'ATC', 'ATA'):'I', ('ATG'):'M', ('GTT', 'GTC', 'GTA', 'GTG'):'V', ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'):'S',('CCT', 'CCC', 'CCA', 'CCG'):'P', ('ACT', 'ACC', 'ACA', 'ACG'):'T', ('GCT', 'GCC', 'GCA', 'GCG'):'A', ('TAT', 'TAC'):'Y', ('CAT', 'CAC'):'H', ('CAA', 'CAG'):'Q', ('AAT', 'AAC'):'N', ('AAA', 'AAG'):'K', ('GAT', 'GAC'):'D', ('GAA', 'GAG'):'E',('TGT', 'TGC'):'C', ('TGG'):'W', ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'):'R', ('GGT', 'GGC', 'GGA', 'GGG'):'G'}

f = open("rosalind_ba4a.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1][0]
RNA = []
for base in data:
    if base == 'U':
        RNA.append('T')
    else:
        RNA.append(base)
RNA_input = ''.join(RNA)

#print (RNA_input)

def translation(RNA):
    protein = ''
    for i in range(0, len(RNA)-2, 3):
        codon = RNA[i:i+3]
        for key in amino_acid:
            if codon in key:
                protein = protein + amino_acid[key]
        
    return protein[:-1]

print (translation(RNA_input))
