f = open("rosalind_ba8a.txt", 'r')
data = f.readlines()

def data_processing(data):
    k = list(map(int, data[0].strip().split(' ')))[0]
    m = list(map(int, data[0].strip().split(' ')))[1]
    points = []
    for coordinate in data[1:]:
        point = list(map(float, coordinate.strip().split(' ')))
        points.append(point)

    return k, m, points

k, m, points = data_processing(data)

def euclidean_distance(point_1, point_2):
    square_sum = 0
    for i in range(len(point_1)):
        square_sum += (point_1[i] - point_2[i])**2
    return square_sum**(1/2)

#print (euclidean_distance([0, 1, 2], [2, 3, 4]))

def find_new_center(points, centers): #both come in [[1, 2], [2, 3], [3, 4], ... ]
    min_distance = []
    for point in points:
        min_distance_temp = 999999999
        for center in centers:
            distance = euclidean_distance(point, center)
            if distance < min_distance_temp:
                min_distance_temp = distance
        min_distance.append(min_distance_temp)
    max_min_distance = max(min_distance)
    next_center = points[min_distance.index(max_min_distance)]
    return next_center

#print (find_new_center([[1, 2], [2, 3], [3, 4], [4, 5]], [[5, 6]]))

def FFT(points, k):
    centers = [points[0]]
    points.remove(centers[0])

    while len(centers)<k:
        new_center = find_new_center(points, centers)
        centers.append(new_center)
        points.remove(new_center)

    return centers

answer = FFT(points, k)
for center in answer:
    print (' '.join(map(str, center)))