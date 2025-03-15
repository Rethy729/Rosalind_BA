f = open('rosalind_ba9f.txt', 'r')
data = f.readlines()
text_1 = data[0].strip()
text_2 = data[1].strip()
text = text_1 + '$' + text_2
#print (text_2)

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
def suffix_addition(text, letter): #this builds a list with all suffices of text + letter added
    answer = []
    for i in range(len(text)):
        answer.append(text[i:]+letter)
    return answer

def longest_common_prefix(text, suffix_array):
    common_prefix_lst = []
    non_shared_substring_candidate = []
    for i in range(1, len(text)):
        suffix_1 = text[suffix_array[i]:]
        suffix_2 = text[suffix_array[i-1]:]
        if ('$' in suffix_1 and '$' not in suffix_2) or ('$' not in suffix_1 and '$' in suffix_2):
            h = 0
            common_prefix = ''
            while h<len(suffix_1) and h<len(suffix_2) and suffix_1[h] == suffix_2[h]:
                common_prefix += suffix_1[h]
                common_prefix_lst.append(common_prefix)
                h += 1
            if '$' in suffix_1 and suffix_1[h] != '$':
                non_shared_substring_candidate += suffix_addition(common_prefix, suffix_1[h])
            elif '$' in suffix_2 and suffix_2[h] != '$':
                non_shared_substring_candidate += suffix_addition(common_prefix, suffix_2[h])

            if common_prefix != '':
                common_prefix_lst.append(common_prefix)
    #print (common_prefix_lst)
    #print (non_shared_substring_candidate)
    non_shared_substring = list(set(non_shared_substring_candidate) - set(common_prefix_lst))
    #print (non_shared_substring)
    return min(non_shared_substring, key=len)

print (longest_common_prefix(text, suffix_array))