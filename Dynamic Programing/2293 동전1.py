import sys
input = sys.stdin.readline
n, k = map(int, input().split())
values = []
for i in range(n):
    values.append(int(input()))

# i원이 되는 경우의 수
dp = [0] * (k+1)
dp[0] = 1

for value in values:
    for i in range(1, k+1):  # i원
        if i - value >= 0:
            dp[i] += dp[i-value]  # i-value원을 만드는 경우의 수만큼 추가
    # print(dp)
print(dp[k])
