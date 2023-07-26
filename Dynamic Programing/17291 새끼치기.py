from sys import stdin
N = int(stdin.readline())

# i가 홀수일 때, i년생 -> i + 4 사망, i - 1년생 -> i + 4 사망
# i + 4년 사망 수 = i년생 + i - 1 년생 수
# j = i + 4일 때, j년 사망 수 = j-4년생 + j-5년생 수

# i년에 태어난 벌레의 수
dp = [0] * (21)
dp[0], dp[1] = 1, 1  # dp[0]-> dp[4] 계산시 필요

for i in range(2, N+1):
    # 분열
    dp[i] = dp[i-1]*2
    # 사망
    dp[i] -= dp[i-4] + dp[i-5] if not i % 2 else 0
print(dp[N])
