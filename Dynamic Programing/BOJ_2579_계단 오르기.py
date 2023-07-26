import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0] * (n+2)
dp[1] = stairs[1]
dp[2] = dp[1] + stairs[2]

for i in range(3, n+1):
    # i번쨰 계단을 2칸으로 올라온 경우, 1칸으로 올라온 경우
    # 이때 1칸으로 올라오기 위해서는 반드시 바로 직전에 2칸으로 올라와야 한다.
    # 즉, 2칸+1칸으로 총 3칸 이전에서 올라와야 한다.
    # 따라서 2칸 전의 dp값  vs 3칸 전의 dp값 + 1칸 전의 점수(2칸오르고 1칸 오름)
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
print(dp[n])
