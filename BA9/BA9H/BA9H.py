f = open('rosalind_ba9h.txt', 'r')
data = f.readlines()

def data_processing(data):
    text = data[0].strip()
    patterns = []
    for line in data[1:]:
        patterns.append(line.strip())
    return text, patterns

text, patterns = data_processing(data)

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

suffix_array = suffix_array(text)

def pattern_matching (text, pattern, suffix_array):

    min_index = 0
    max_index = len(text)
    while min_index < max_index:
        mid_index = (min_index+max_index)//2
        if pattern > text[suffix_array[mid_index]:suffix_array[mid_index]+len(pattern)]: #this does not make index error because when a='abcde', a[2:6]=a[2:10]=a[2:100]='cde'
            min_index = mid_index + 1
        else:
            max_index = mid_index
    first_index = min_index
    max_index = len(text)

    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if pattern < text[suffix_array[mid_index]:suffix_array[mid_index]+len(pattern)]:
            max_index = mid_index
        else:
            min_index = mid_index + 1
    last_index = max_index

    if first_index > last_index:
        return
    else:
        return suffix_array[first_index:last_index]

answer_lst = []
for pattern in patterns:
    answer = pattern_matching(text, pattern, suffix_array)
    if answer != None:
        answer_lst += answer
print (' '.join(map(str, answer_lst)))