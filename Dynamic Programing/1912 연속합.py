import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
size = len(numbers)
dp = [-1001] * (size+1)
dp[0] = numbers[0]


# 이 경우는 손해보더라도 일단 더하고 뒤에서 보상받는 케이스를 커버 못 함
# for i, num in enumerate(numbers): # dp[i] 게산 - 연속된 수열
#     for x in range(i+1, size):
#         sum = numbers[i] + numbers[x]
#         if sum < dp[i]: # 다음 수를 더했을 때 손해
#             break
#         else:
#             dp[i] = sum


# dp[i-1] + num vs num
dp[0] = numbers[0]
for i in range(1, size):
    dp[i] = max(numbers[i], dp[i-1]+numbers[i])
    
print(max(dp))

# 29분