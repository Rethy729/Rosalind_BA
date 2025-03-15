from collections import defaultdict

f = open('rosalind_ba9a.txt', 'r')
data = f.readlines()

def data_processing(data):
    patterns = []
    for line in data:
        patterns.append(line.strip())
    return patterns

patterns = data_processing(data)

def trie_construction(patterns):
    root = 0
    trie = defaultdict(dict)
    new_node = 1
    for pattern in patterns:
        current_node = root
        for letter in pattern:
            if current_node in trie[letter]:
                current_node = trie[letter][current_node]
            else:
                trie[str(letter)][current_node] = new_node
                current_node = new_node
                new_node += 1
    return trie #{symbol:{node:node}}

answer = trie_construction(patterns)
print (answer)
edges = []
for key in answer:
    for node in answer[key]:
        edges.append([node, answer[key][node], key])
edges.sort()
for edge in edges:
    print (str(edge[0])+'->'+str(edge[1])+':'+str(edge[2]))