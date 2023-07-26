# import sys

# input = sys.stdin.readline

# N = int(input())
# num_list = list(map(int, input().split()))
# operater_list = list(map(int, input().split()))

# plus, minus, multiply, divide = operater_list[0], operater_list[1], operater_list[2], operater_list[3]

# maxNum = -1e9
# minNum = 1e9


# def dfs(depth, result, plus, minus, multiply, divide):
#     global maxNum, minNum
#     if depth == N:
#         maxNum = max(maxNum, result)
#         minNum = min(minNum, result)
#         return
#     if plus:
#         dfs(depth+1, result + num_list[depth],
#             plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth+1, result - num_list[depth],
#             plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth+1, result*num_list[depth], plus, minus, multiply-1, divide)
#     if divide:
#         dfs(depth+1, int(result/num_list[depth]),
#             plus, minus, multiply, divide-1)


# dfs(1, num_list[0], plus, minus, multiply, divide)
# print(maxNum)
# print(minNum)

n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9


def DFS(depth, arr):
    global add, sub, mul, div, max_value, min_value

    if depth == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            DFS(depth+1, arr + data[depth])
            add += 1
        if sub > 0:
            sub -= 1
            DFS(depth+1, arr - data[depth])
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(depth+1, arr*data[depth])
            mul += 1
        if div > 0:
            div -= 1
            DFS(depth+1, int(arr/data[depth]))
            div += 1


DFS(1, data[0])

print(max_value)
print(min_value)
