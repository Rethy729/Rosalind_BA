f = open("rosalind_ba8c.txt", 'r')
data = f.readlines()

def data_processing(data):
    k = list(map(int, data[0].strip().split(' ')))[0]

    points = []
    for coordinate in data[1:]:
        point = list(map(float, coordinate.strip().split(' ')))
        points.append(point)

    centers = points[:k]
    return k, points

k, points = data_processing(data)

def euclidean_distance(point_1, point_2):
    square_sum = 0
    for i in range(len(point_1)):
        square_sum += (point_1[i] - point_2[i])**2
    return square_sum**(1/2)

def new_center_gen(clusters, centers):
    new_centers = []
    for i, cluster in enumerate(clusters):
        if len(clusters) == 0:
            new_centers.append(centers[i])
        else:
            new_center_temp = []
            for i in range(len(cluster[0])):
                sum_temp = 0
                for point in cluster:
                    sum_temp += point[i]
                new_center_temp.append(round(sum_temp/len(cluster), 3))
            new_centers.append(new_center_temp)
    return new_centers

def Lloyd(points, k):

    centers = points[:k]

    for _ in range(30):
        clusters = []
        for i in range(k):
            clusters.append([])

        for point in points:
            min_distance = 999999999
            center_index = 0
            for i, center in enumerate(centers):
                distance = euclidean_distance(point, center)
                if distance < min_distance:
                    min_distance = distance
                    center_index = i
            clusters[center_index].append(point)
        centers = (new_center_gen(clusters, centers))

    return (centers)

answer = Lloyd(points, k)
for point in answer:
    print (' '.join(map(str, point)))
