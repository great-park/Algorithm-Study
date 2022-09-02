from sys import stdin
input = stdin.readline
N = int(input())
budget_req_list = list(map(int, input().split()))
total_budget = int(input())
start, end = 0, max(budget_req_list)

while start <= end:
    mid = (start + end) // 2  # 상한액
    sum = 0
    for each_budget_req in budget_req_list:
        if each_budget_req <= mid:
            sum += each_budget_req
        else:
            # 상한액을 넘으면 상한액까지만
            sum += mid
    if sum <= total_budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)
