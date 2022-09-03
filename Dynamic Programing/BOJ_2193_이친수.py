from sys import stdin
input = stdin.readline
N = int(input())

"""
n
1 - 1
2 - 10
3 - 101, 100
4 - 1010, 1001, 1000
5 - 10101, 10100, 10010, 10001, 10000
"""
dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 1
for i in range(3, N+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[N])
