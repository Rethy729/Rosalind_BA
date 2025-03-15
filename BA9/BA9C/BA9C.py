from collections import defaultdict

f = open('rosalind_ba9c.txt', 'r')
data = f.readlines()
text = data[0].strip()

def modified_trie_construction(text):
    root = 0
    trie = defaultdict(dict)
    new_node = 1
    for i in range(len(text)):
        current_node = root
        for j in range(i, len(text)):
            current_symbol = text[j]
            if current_symbol in trie[current_node]:
                current_node = trie[current_node][current_symbol]
            else:
                trie[current_node][current_symbol] = new_node
                current_node = new_node
                new_node += 1
    return trie #{node:{symbol:node}}

text_trie = modified_trie_construction(text)
print (text_trie)

def find_edge(current_node, edge, trie):
    if len(trie[current_node]) == 0:
        edges.append(edge)
        return

    if len(trie[current_node])>=2 and edge!='':
        edges.append(edge)
        edge = ''

    for symbol, arr_node in trie[current_node].items():
        find_edge(arr_node, edge+symbol, trie)

edges = []
find_edge(0, '', text_trie)

for edge in edges:
    print (edge)


