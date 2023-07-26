import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = list()

for i in range(n):
    coins.append(int(input()))

dp = [100001] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
        print(i, dp[i])

if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)

# 15분