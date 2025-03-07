f = open("rosalind_ba1l.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

PtN = {'A':0, 'C':1, 'G':2, 'T':3}
template = list(data[0])

def Pattern_To_Number(string):
    
    if len(string) == 1:
        return PtN[string[0]]

    last_digit = string.pop()
    return Pattern_To_Number(string) * 4 + PtN[last_digit]

print (Pattern_To_Number(template))
