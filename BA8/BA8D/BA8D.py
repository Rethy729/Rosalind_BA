import math

f = open("rosalind_ba8d.txt", 'r')
data = f.readlines()

def data_processing(data):
    k = list(map(int, data[0].strip().split(' ')))[0]
    m = list(map(int, data[0].strip().split(' ')))[1]
    sp = float(data[1])
    points = []
    for coordinate in data[2:]:
        point = list(map(float, coordinate.strip().split(' ')))
        points.append(point)
    return k, m, sp, points

k, m, sp, points = data_processing(data)

def euclidean_distance(point_1, point_2):
    square_sum = 0
    for i in range(len(point_1)):
        square_sum += (point_1[i] - point_2[i])**2
    return square_sum**(1/2)

def dot_product(lst_1, lst_2):
    dot = 0
    for i in range(len(lst_1)):
        dot += (lst_1[i])*(lst_2[i])
    return dot

def hidden_matrix_gen(sp, points, centers):

    hidden_matrix = []
    for i in range(len(centers)):
        hidden_matrix.append([0]*len(points))

    for i in range(len(points)):
        e_distance = []
        for j in range(len(centers)):
            e_distance.append(math.e**((-sp)*euclidean_distance(points[i], centers[j])))
        sum_e_distance = sum(e_distance)

        for j in range(len(centers)):
            e_distance[j] = (e_distance[j]/sum_e_distance)

        for j in range(len(centers)):
            hidden_matrix[j][i] = e_distance[j]
    return hidden_matrix

#hidden_matrix_gen(k, m, sp, points, points[:2])

def new_center_gen(m, hidden_matrix, points, centers):
    new_center = []
    for i in range(len(centers)):
        new_center_temp = []
        for j in range(m):
            jth_elements = []
            for point in points:
                jth_elements.append(point[j])
            new_center_temp.append(dot_product(hidden_matrix[i], jth_elements)/dot_product(hidden_matrix[i], [1]*len(points)))
        new_center.append(new_center_temp)
    return new_center

def k_means_clustering(k, m, sp, points):

    centers = points[:k]
    for _ in range(100):
        hidden_matrix = hidden_matrix_gen(sp, points, centers)
        centers = new_center_gen(m, hidden_matrix, points, centers)
    return centers

answer = k_means_clustering(k, m, sp, points)
for i in range(k):
    for j in range(m):
        answer[i][j] = round(answer[i][j], 3)
for point in answer:
    print (' '.join(map(str, point)))