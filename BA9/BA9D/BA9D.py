f = open('rosalind_ba9d.txt', 'r')
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
    return suffix_array

suffix_array = suffix_array(text)

def longest_common_prefix(text, suffix_array):
    common_prefix_lst = []
    for i in range(1, len(text)):
        suffix_1 = text[suffix_array[i]:]
        suffix_2 = text[suffix_array[i-1]:]
        h = 0
        common_prefix = ''
        while h<len(suffix_1) and h<len(suffix_2) and suffix_1[h] == suffix_2[h]:
            common_prefix += suffix_1[h]
            h += 1
        if common_prefix != '':
            common_prefix_lst.append(common_prefix)
    if len(common_prefix_lst) != 0:
        return max(common_prefix_lst, key = len)
    else:
        return 'No repeat'

print (longest_common_prefix(text, suffix_array))

