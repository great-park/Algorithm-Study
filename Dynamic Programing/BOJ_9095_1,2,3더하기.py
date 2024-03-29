from sys import stdin
input = stdin.readline
N = int(input())
"""
패턴 찾기
dp[1] = 1
dp[2] = 2
dp[3] = 4  : 1+1+1, 1+2, 2+1, 3
dp[4] = 7  : 1+1+1+1,  1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
dp[5] = 13 : 1+1+1+1+1, 1+2 * 5개, 2+2+1 * 3개, 3+1+1 *3게, 3+2
dp[6] = 24 : 1+1+1+1+1+1, 1+2*5개, 2+2+1+1 * 6개, 3+1+1+1*4개, 3+2+1 6개, 3+3 1개
dp[7] = 44
"""


def solve(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return solve(x-1) + solve(x-2) + solve(x-3)


for i in range(N):
    num = int(input())
    print(solve(num))

########################################
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1)

    for i in range(1, N+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])
