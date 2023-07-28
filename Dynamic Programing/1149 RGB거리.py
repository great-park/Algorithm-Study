import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]


# 그냥 i번째에 대해서 각 색깔 집을 선택했을 때 가장 최소 비용을 저장한다.
for i in range(1, N):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
    cost[i][2] = cost[i][2] + min(cost[i-1][0], cost[i-1][1])

print(min(cost[N-1]))

# 50분




# 실패 
## dp[i-2] 까지는 최소 비용이 보장, i-1과 i 사이의 3*2 = 6가지의 경우의 수에서 i-2와 같은 색을 선택하는 i-1번째 경우의 수를 제외하여 총 4가지 경우의 수 비교
# print(f'dp[1]: {dp[1]}')
# for i in range(2, N):
#     dp[i] = dp[i-2] + min(cost[i-1][0]+ cost[i][1], 
#                             cost[i-1][0]+ cost[i][2], 
#                             cost[i-1][1]+ cost[i][0], 
#                             cost[i-1][1]+ cost[i][2], 
#                             cost[i-1][2]+ cost[i][0], 
#                             cost[i-1][2]+ cost[i][1])
    
#     print(f'{i}번째 :{dp[i]}')
    
# print(dp[N-1])

