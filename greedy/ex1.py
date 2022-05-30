exchange = int(input())
coin_list = [500, 100, 50, 10]
count = 0

for coin in coin_list:
    count += exchange//coin
    exchange -= coin*(exchange//coin)

print(count)