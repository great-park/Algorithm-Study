N = int(input())

# 연산 횟수 저장 -> 앞에서 구한 값을 저장하고 후에 사용하기
dp = [0]*(N+1)  # 인덱스 맞추기 위해 N+1

for i in range(2, N+1):
    # case 1. 1을 빼는 연산 ex) 10이면, 9인 경우에 1 더한 값
    dp[i] = dp[i-1] + 1

    # case 2. 2를 나누는 연산. case1과 비교하여 작은 값을 저장
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # case 3. 3을 나누는 연산. case1, case2와 비교하여 작은 값을 저장
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
