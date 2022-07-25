from sys import stdin
input = stdin.readline
N = int(input())
budget_req = list(map(int, input().split()))
total_budget = int(input())
start, end = 0, max(budget_req)

while start <= end:
    mid = (start + end) // 2  # 상한액
    possible_budget = 0
    for req in budget_req:
        if req <= mid:
            possible_budget += req
        else:
            # 상한액을 넘으면 상한액까지만
            possible_budget += mid
    if possible_budget <= total_budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)
