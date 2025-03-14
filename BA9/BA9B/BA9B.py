from collections import defaultdict

f = open('rosalind_ba9b.txt', 'r')
data = f.readlines()

def data_processing(data):
    text = data[0].strip()
    patterns = []
    for line in data[1:]:
        patterns.append(line.strip())
    return text, patterns

text, patterns = data_processing(data)

def trie_construction(patterns):
    root = 0
    trie = defaultdict(dict)
    new_node = 1
    leaf_nodes = []
    for pattern in patterns:
        current_node = root
        for i, letter in enumerate(pattern):
            if current_node in trie[letter]:
                current_node = trie[letter][current_node]
            else:
                trie[str(letter)][current_node] = new_node
                current_node = new_node
                if i == len(pattern) - 1:
                    leaf_nodes.append(current_node)
                new_node += 1
    return trie, leaf_nodes

pattern_trie, leaf_nodes = trie_construction(patterns)
print (pattern_trie)
print (leaf_nodes)

def prefix_trie_matching(text, trie, leaf):

    index = 0
    symbol = text[0]
    v = 0
    while True:
        if v in leaf:
            print (v)
            return True

        elif index == len(text):
            return False

        elif (symbol in trie) and (v in trie[symbol]):
            index += 1
            v = trie[symbol][v]
            if index == len(text):
                continue
            symbol = text[index]

        else:
            return False

def trie_matching(text, trie, leaf):
    answer = []
    index = 0
    while text != '':
        print (text)
        if prefix_trie_matching(text, trie, leaf):
            answer.append(index)
        index += 1
        text = text[1:]
    return answer
print (' '.join(map(str, trie_matching(text, pattern_trie, leaf_nodes))))
