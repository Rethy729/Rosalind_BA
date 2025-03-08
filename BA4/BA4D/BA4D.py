m = int(input())

ProteinMass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def counting_peptides(n):
    counting_lst = [0] * (n+1)
    counting_lst[0] = 1
    for i in range(1, n+1):
        for mass in ProteinMass:
            num = 0
            if i >= mass:
                num += counting_lst[i-mass]
            counting_lst[i] += num
    return counting_lst[n]

print (counting_peptides(m))



