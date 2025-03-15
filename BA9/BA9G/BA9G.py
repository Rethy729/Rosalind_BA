f = open('rosalind_ba9g.txt', 'r')
data = f.readlines()
text = data[0].strip()
print (text)

def sort_key(string):
    return string.replace('$', ' ')

def suffix_array(text):
    suffix_lst = []
    suffix_dict = {}

    for i in range(len(text)):
        suffix_lst.append(text[i:])
        suffix_dict[text[i:]] = i

    sorted_suffix_lst = sorted(suffix_lst, key = sort_key)

    suffix_array = []
    for suffix in sorted_suffix_lst:
        suffix_array.append(suffix_dict[suffix])
    return (suffix_array)

answer = suffix_array(text)
print (', '.join(map(str, answer)))