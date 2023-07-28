import sys
input = sys.stdin.readline

def bridge(n,m):
    dp = [[0] *(m+1) for _ in range(n+1)]

    for i in range(1,m+1):
        dp[1][i] = i # N이 1인 경우는 모두 M개만큼 경우의 수가 존재

    for j in range(2,n+1): 
        for k in range(j,m+1):
            for l in range(j-1, k):
                dp[j][k] += dp[j-1][l]

    return dp[n][m]

T = int(input())

for _ in range(T):          
    n, m = map(int,input().rstrip().rsplit())
    print(bridge(n,m))  