f = open("rosalind_ba5a.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
money = int(data[0])
coins = list(map(int, data[1].split(',')))

def pay(money, coins):

    payment = [money+1] * (money + 1)
    payment[0] = 0
    for coin in coins:
        if money >= coin:
            for i in range(coin, money+1):
                payment[i] = min(payment[i], payment[i-coin]+1)

    return payment[money]

print (pay(money, coins))
                
