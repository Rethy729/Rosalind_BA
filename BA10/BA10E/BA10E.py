f = open('rosalind_ba10e.txt', 'r')
data = f.readlines()

def data_processing(data):
    theta = float(data[0])
    sym = list(map(str, data[2].strip().split()))
    align_matrix = []
    for line in data[4:]:
        if line != '':
            align_matrix.append(line.strip())

    #print (theta)
    #print (sym)
    #print (align_matrix)
    exclude_column = []
    include_column = []
    align_num = len(align_matrix)
    for i in range(len(align_matrix[0])):
        count = 0
        for line in align_matrix:
            if line[i] == '-':
                count += 1
        if (count/align_num) > theta:
            exclude_column.append(i)
        else:
            include_column.append(i)
    #print (include_column)
    #print (exclude_column)

    return sym, align_matrix, include_column, exclude_column

sym, align_matrix, include_column, exclude_column = data_processing(data)

def HMM_gen(sym, align_matrix, include_column, exclude_column):

    length = len(align_matrix[0])

    row_index = ['S','I0']
    for i in range(1, length+1-len(exclude_column)):
        row_index.append('M' + str(i))
        row_index.append('D' + str(i))
        row_index.append('I' + str(i))
    row_index.append('E')
    #print (row_index)

    transition_matrix = []
    for i in range(len(row_index)):
        transition_matrix.append([0]*len(row_index))

    emission_matrix = []
    for i in range(len(row_index)):
        emission_matrix.append([0] * len(sym))
    print(emission_matrix)

    exclude_column_index = []
    for i in range(len(exclude_column)):
        count = 0
        for j in range(exclude_column[i], -1, -1):
            if j in include_column:
                exclude_column_index.append((exclude_column[i], j))
                break
            else:
                count += 1
        if count == exclude_column[i]+1:
            exclude_column_index.append((exclude_column[i], 'x'))

    #print (exclude_column_index)

    HMM_route = []
    for line in align_matrix:
        HMM = ['S']
        string_1 = line
        for i in range(length):
            if i in include_column:
                if string_1[i] != '-':
                    HMM.append('M' + str(include_column.index(i) + 1))
                    emission_matrix[row_index.index(HMM[-1])][sym.index(string_1[i])] += 1
                else:
                    HMM.append('D' + str(include_column.index(i) + 1))
            else:
                if string_1[i] != '-':
                    if exclude_column_index[exclude_column.index(i)][1] != 'x':
                        HMM.append('I' + str(include_column.index(exclude_column_index[exclude_column.index(i)][1])+1))
                        emission_matrix[row_index.index(HMM[-1])][sym.index(string_1[i])] += 1
                    else:
                        HMM.append('I0')
                        emission_matrix[row_index.index(HMM[-1])][sym.index(string_1[i])] += 1
        HMM.append('E')
        HMM_route.append(HMM)

    #print (HMM_route)
    print (emission_matrix)

    for i in range(len(HMM_route)):
        for j in range(len(HMM_route[i])-1):
            start = HMM_route[i][j:j+2][0]
            end = HMM_route[i][j:j+2][1]
            transition_matrix[row_index.index(start)][row_index.index(end)] += 1
    #print (transition_matrix)

    for row in transition_matrix:
        row_sum = sum(row)
        for i in range(len(row)):
            if row_sum != 0:
                row[i] = row[i]/row_sum
            else:
                continue
    #print(transition_matrix)

    for row in emission_matrix:
        row_sum = sum(row)
        for i in range(len(row)):
            if row_sum != 0:
                row[i] = row[i] / row_sum
            else:
                continue
    #print (emission_matrix)

    return transition_matrix, emission_matrix, row_index

transition_matrix, emission_matrix, row_index = HMM_gen(sym, align_matrix, include_column, exclude_column)

w = open('output_ba10e.txt', 'w')
w.write(' '.join(map(str, row_index))+'\n')
for i in range(len(row_index)):
    if i == len(row_index)-1:
        w.write(row_index[i] + ' '+ ' '.join(map(str, transition_matrix[i]))+'\n'+'--------')
    else:
        w.write(row_index[i] + ' ' + ' '.join(map(str, transition_matrix[i])) + '\n')
w.write('\n')
w.write(' '.join(map(str, sym))+'\n')
for i in range(len(row_index)):
    w.write(row_index[i] + ' ' + ' '.join(map(str, emission_matrix[i])) + '\n')
w.close()