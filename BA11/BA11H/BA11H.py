f = open('rosalind_ba11h.txt', 'r')
data = f.readlines()

def data_processing(data):
    spectrum = list(map(int, data[0].strip().split()))
    threshold = int(data[1])
    max_score = int(data[2])
    return spectrum, threshold, max_score

spectrum, threshold, max_score = data_processing(data)

def size_dict(spectrum, threshold, max_score):
    #matrix generation
    max_spec = 0
    min_spec = 0
    for num in spectrum:
        if num>0:
            max_spec += num
        else:
            min_spec += num
    height = max_spec + 1 + -min_spec
    spectrum = [0] + spectrum
    matrix = []
    for _ in range(height):
        matrix.append([0 for _ in range(len(spectrum))])
    #matrix initialization
    for i in range(len(matrix)):
        for j in range(57):
            matrix[i][j] = 0
    matrix[0][0] = 1
    #recursion
    for i in range(57, len(matrix[0])):
        spec_score = spectrum[i]
        possible_aa = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
        if i >= 186:
            possible_aa = possible_aa
        else:
            index = 0
            for aa in possible_aa:
                if i < aa:
                    index = possible_aa.index(aa)
                    break
            possible_aa = possible_aa[:index]

        for j in range(len(matrix)):
            if (j-spec_score) < 0 or (j-spec_score)>=len(matrix):
                continue
            score_lst = []
            for aa in possible_aa:
                if aa == 113 or aa == 128:
                    score_lst.append(2 * matrix[j - spec_score][i - aa])
                else:
                    score_lst.append(matrix[j-spec_score][i-aa])
            matrix[j][i] = sum(score_lst)
    #count the dict_count
    dict_count = 0
    for i in range(threshold, max_score+1):
        dict_count += matrix[i][-1]
    return dict_count

answer = size_dict(spectrum, threshold, max_score)
print (answer)