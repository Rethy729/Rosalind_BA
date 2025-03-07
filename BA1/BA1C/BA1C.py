f = open("rosalind_ba1c.txt", 'r')
raw_data = f.read()
DNA_sequence = raw_data.split('\n')[0]

complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

reverse = ""

for base in DNA_sequence:
    reverse = complement[base] + reverse

w = open("output_ba1c.txt", 'w')
w.write(reverse)
w.close()
