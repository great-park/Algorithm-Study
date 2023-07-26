import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
tmp = [-1000000001]
maxVal = 0

for i in range(1, n + 1):
    if tmp[-1] < a[i]:  # tmp에 저장된 부분 수열 마지막 수보다 현재 수가 크다면
        tmp.append(a[i])  # 부분 수열의 마지막에 현재 수를 추가하고
        dp[i] = len(tmp) - 1  # 부분 수열의 길이를 dp에 저장해주고
        maxVal = dp[i]  # 부분 수열의 최대 길이를 갱신해준다.
    else:
        dp[i] = bisect_left(tmp, a[i])  # tmp에서 현재 수가 어디에 위치하는지 찾아서
        tmp[dp[i]] = a[i]  # 해당 위치의 수를 현재 수로 갱신해준다.

print(maxVal)

# 연산이 완료되면 dp[i]에는 a[i]가 마지막인 부분 수열의 최대 길이가 저장되어있다.
tmp2 = []
for i in range(n, 0, -1):
    if dp[i] == maxVal:
        tmp2.append(a[i])
        maxVal -= 1
print(*tmp2[::-1])

# 출처 : https://ca.ramel.be/105
