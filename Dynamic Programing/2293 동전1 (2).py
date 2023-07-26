import sys
input = sys.stdin.readline
n,k = map(int, input().split())

dp = [0]*100001
dp[0] = 1

coins = list()
for i in range(n):
    coins.append(int(input()))

for coin in coins:
    for id in range(coin, k+1):
        dp[id] += dp[id-coin]

print(dp[id])

# 11분