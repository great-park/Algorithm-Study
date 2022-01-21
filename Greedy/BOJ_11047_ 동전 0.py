# (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
import sys

N, K = map(int, sys.stdin.readline().split())

coin_value_list = list()

for i in range(N):
    coin_value = int(input())
    coin_value_list.append(coin_value)
coin_value_list.sort(reverse=True)
count = 0

for coin_value in coin_value_list:
    if coin_value <= K:
        count += K//coin_value
        K -= coin_value * (K//coin_value)

print(count)
