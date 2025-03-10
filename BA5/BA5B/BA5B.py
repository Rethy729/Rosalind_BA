f = open("rosalind_ba5b.txt", 'r')
data = f.readlines()
n = list(map(int, data[0].split(' ')))[0]
m = list(map(int, data[0].split(' ')))[1]

def make_matrix(data):
    hori = []
    verti = []
    for i in range(n):
        verti.append(list(map(int, data[i+1].split(' '))))
    for j in range(n+1):
        hori.append(list(map(int, data[j+1+n+1].split(' '))))
    return hori, verti

hori, verti = (make_matrix(data))
#print (verti)
#print (hori)

def MaxDistance(h, v): #h for hori, v for verti
    distance_lst = []
    for i in range(n+1):
        distance_lst.append([0]*(m+1))

    #print(distance_lst)
    hori_sum = 0
    for i in range(m):
        hori_sum += h[0][i]
        distance_lst[0][i+1] = hori_sum
    #print(distance_lst)
    verti_sum = 0
    for i in range(n):
        verti_sum += v[i][0]
        distance_lst[i+1][0] = verti_sum
    #print(distance_lst)

    for i in range(1, n+1):
        for j in range(1, m+1):
            distance_lst[i][j] = max(distance_lst[i-1][j]+verti[i-1][j], distance_lst[i][j-1]+hori[i][j-1])

    return(distance_lst[n][m])

print(MaxDistance(hori, verti))