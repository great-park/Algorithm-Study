from sys import stdin
input = stdin.readline
price = int(input())
price = 1000 - price
coin = [500, 100, 50, 10, 5, 1]
cnt = 0
while price != 0:
    if price - coin[0] >= 0:
        price -= coin[0]
    elif price - coin[1] >= 0:
        price -= coin[1]
    elif price - coin[2] >= 0:
        price -= coin[2]
    elif price - coin[3] >= 0:
        price -= coin[3]
    elif price - coin[4] >= 0:
        price -= coin[4]
    elif price - coin[5] >= 0:
        price -= coin[5]
    cnt += 1
print(cnt)
