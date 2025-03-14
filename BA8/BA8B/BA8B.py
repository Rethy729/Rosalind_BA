f = open("rosalind_ba8b.txt", 'r')
data = f.readlines()

def data_processing(data):
    k = list(map(int, data[0].strip().split(' ')))[0]
    m = list(map(int, data[0].strip().split(' ')))[1]

    centers = []
    points = []

    for coordinate in data[1:1+k]:
        point = list(map(float, coordinate.strip().split(' ')))
        centers.append(point)
    for coordinate in data[2+k:]:
        point = list(map(float, coordinate.strip().split(' ')))
        points.append(point)

    return k, centers, points

k, centers, points = data_processing(data)

def euclidean_distance(point_1, point_2):
    square_sum = 0
    for i in range(len(point_1)):
        square_sum += (point_1[i] - point_2[i])**2
    return square_sum**(1/2)

def squared_error_distortion(points, centers):

    distance_square_sum = 0

    for point in points:
        min_distance = 999999999
        for center in centers:
            distance = euclidean_distance(point, center)
            if distance < min_distance:
                min_distance = distance
        distance_square_sum += (min_distance)**2

    return distance_square_sum/len(points)

print (round(squared_error_distortion(points, centers), 3))