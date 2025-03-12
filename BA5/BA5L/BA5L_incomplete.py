f = open('BLOSUM62.txt', 'r')
data = f.readlines()
char_lst = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','-']
BLOSUM62 = []
for line in data[1:]:
    BLOSUM62.append(list(map(int, line.split())))
#print (BLOSUM62)

f = open('rosalind_ba5l.txt', 'r')
data = f.readlines()
string_1 = (list(map(str, data[0].strip())))
string_2 = (list(map(str, data[1].strip())))

indel = -5 #score of indel

def matrix_maker(str2, str1, score): #str1 is horizontal, str2 is vertical
    diago = []
    for i in range(len(str2)):
        diago_row = []
        char_2 = str2[i]
        char_2_index = char_lst.index(char_2)
        for j in range(len(str1)):
            char_1 = str1[j]
            char_1_index = char_lst.index(char_1)
            diago_row.append(score[char_1_index][char_2_index])
        diago.append(diago_row)
    return diago

def Backtracking(score):
    route = ''
    sii = len(score)-1 #sii = start_index_i
    sij = len(score[0])-1 #sij = start_index_j

    while sii != 0 and sij != 0:
        if score[sii][sij] == score[sii-1][sij] + indel:
            route = 'd' + route
            sii = sii - 1
        elif score[sii][sij] == score[sii][sij-1] + indel:
            route = 'i' + route
            sij = sij - 1
        else:
            route = 'm' + route
            sii = sii - 1
            sij = sij - 1
    for i in range(sii):
        route = 'd' + route
    for i in range(sij):
        route = 'i' + route
    return route

def MidNode_and_MidEdge(top, bottom, left, right, h_string, v_string, score): #gets the h_string as the horizontal string, therefore h_string is the first string of the result.

    h_str = h_string[left:right]
    #print (h_str)
    v_str = v_string[top:bottom]
    #print (v_str)

    diago = matrix_maker(v_str, h_str, score)
    n = 2              #the horizontal length of the matrix
    m = (bottom-top)+1 #the vertical length of the matrix
    middle = (left + right) // 2
    score_matrix = []
    #initializing
    for i in range(m):
        score_matrix.append([-99999999] * n)
    for i in range(n):
        score_matrix[0][i] = (indel) * i
    for i in range(m):
        score_matrix[i][0] = (indel) * i
    column_number = left + 1
    while column_number <= middle:
        for i in range(1, m):
            score_matrix[i][1] = max(score_matrix[i - 1][1] + indel, score_matrix[i][0] + indel, score_matrix[i - 1][0] + diago[i - 1][column_number-1-left])
        if column_number == middle:
           break
        for i in range(m):
            score_matrix[i][0] = score_matrix[i][1]
        score_matrix[0][1] = (indel)*(column_number+1)
        for i in range(1, m):
            score_matrix[i][1] = -99999999
        column_number += 1

    #start from the sink
    h_str_rev = h_str[::-1]
    v_str_rev = v_str[::-1]
    new_diago = matrix_maker(v_str_rev, h_str_rev, score)
    n = 2                   # the horizontal length of the matrix
    m = (bottom - top) + 1  # the vertical length of the matrix
    counter_middle = (left+right)-middle
    rev_score_matrix = []
    # initializing
    for i in range(m):
        rev_score_matrix.append([-99999999] * n)
    for i in range(n):
        rev_score_matrix[0][i] = (indel) * i
    for i in range(m):
        rev_score_matrix[i][0] = (indel) * i
    column_number = left + 1
    vector = [1]*(m)
    while column_number <= counter_middle:
        for i in range(1, m):
            cand = [rev_score_matrix[i - 1][1] + indel, rev_score_matrix[i][0] + indel,
                                     rev_score_matrix[i - 1][0] + new_diago[i - 1][column_number - 1-left]] # 1: horizontal move 2:diagonal move
            rev_score_matrix[i][1] = max(cand)
            vector[i] = cand.index(rev_score_matrix[i][1])
        if column_number == counter_middle:
           break
        for i in range(m):
            rev_score_matrix[i][0] = rev_score_matrix[i][1]
        rev_score_matrix[0][1] = (indel) * (column_number + 1)
        for i in range(1, m):
            rev_score_matrix[i][1] = -99999999
        column_number += 1

    #by summing, determine the middle node
    max_sum = -99999999
    max_index = 0
    for i in range(bottom-top+1):
        if max_sum < score_matrix[i][1]+rev_score_matrix[(bottom-top)-i][1]:
            max_sum = score_matrix[i][1]+rev_score_matrix[(bottom-top)-i][1]
            max_index = i + top
    middle_node = [max_index, middle]
    print(max_sum)
    if vector[bottom-max_index] == 2:
        return middle_node, 'm'
    else:
        return middle_node, 'i'

    #print (middle_node)
    #print (next_node)

def LSA(top, bottom, left, right, h_string, v_string, score):

    if top == bottom:
        return 'i'*(right-left)
    if left == right:
        return 'd'*(bottom-top)

    if top+1 == bottom:
        h_str = h_string[left:right]
        v_str = v_string[top:bottom]
        diago = matrix_maker(v_str, h_str, score)
        n = (right - left)+1  # the horizontal length of the matrix
        m = 2                 # the vertical length of the matrix
        score_matrix = []
        for i in range(m):
            score_matrix.append([-99999999] * n)
        for i in range(n):
            score_matrix[0][i] = (indel) * i
        for i in range(m):
            score_matrix[i][0] = (indel) * i
        for i in range(1, n):
            score_matrix[1][i] = max(score_matrix[1][i-1] + indel, score_matrix[0][i] + indel,
                                     score_matrix[0][i-1] + diago[0][i-1])
        route = (Backtracking(score_matrix))
        return route

    if left+1 == right:
        h_str = h_string[left:right]
        v_str = v_string[top:bottom]
        diago = matrix_maker(v_str, h_str, score)
        n = 2                              # the horizontal length of the matrix
        m = (bottom-top) +1                # the vertical length of the matrix
        score_matrix = []
        for i in range(m):
            score_matrix.append([-99999999] * n)
        for i in range(n):
            score_matrix[0][i] = (indel) * i
        for i in range(m):
            score_matrix[i][0] = (indel) * i
        for i in range(1, m):
            score_matrix[i][1] = max(score_matrix[i-1][1] + indel, score_matrix[i][0] + indel,
                                     score_matrix[i-1][0] + diago[i-1][0])
        route = (Backtracking(score_matrix))
        return route

    mid_node, mid_edge = MidNode_and_MidEdge(top, bottom, left, right, h_string, v_string, score)
    route = LSA(top, mid_node[0], left, mid_node[1], h_string, v_string, score)
    route += mid_edge
    if mid_edge == 'm':
        mid_node[0] += 1
        mid_node[1] += 1
    else:
        mid_node[1] += 1
    route += LSA(mid_node[0], bottom, mid_node[1], right, h_string, v_string, score)
    return route

def route_to_alignment(str1, str2, route): #str1 is horizontal, str2 is vertical
    align_str1 = ''
    align_str2 = ''
    index_1 = 0
    index_2 = 0
    for path in route:
        if path == 'm':
            align_str1 += str1[index_1]
            align_str2 += str2[index_2]
            index_1 += 1
            index_2 += 1
        elif path == 'i':
            align_str1 += str1[index_1]
            align_str2 += '-'
            index_1 += 1
        else:
            align_str1 += '-'
            align_str2 += str2[index_2]
            index_2 += 1
    print (align_str1)
    print (align_str2)


#when input, second row of the text is the first row of the result and first row of the text is the second row of the result
horizontal_string = string_2
vertical_string = string_1
MidNode_and_MidEdge(0, len(vertical_string), 0, len(horizontal_string), horizontal_string, vertical_string, BLOSUM62)
rt = LSA(0, len(vertical_string), 0, len(horizontal_string), horizontal_string, vertical_string, BLOSUM62)
route_to_alignment(horizontal_string, vertical_string, rt)