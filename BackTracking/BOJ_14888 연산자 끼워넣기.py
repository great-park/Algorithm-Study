import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
operater_list = list(map(int, input().split()))

plus, minus, multiply, divide = operater_list[0], operater_list[1], operater_list[2], operater_list[3]

maxNum = -1e9
minNum = 1e9


def dfs(depth, result, plus, minus, multiply, divide):
    global maxNum, minNum
    if depth == N:
        maxNum = max(maxNum, result)
        minNum = min(minNum, result)
        return
    if plus:
        dfs(depth+1, result + num_list[depth],
            plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth+1, result - num_list[depth],
            plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth+1, result*num_list[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(result/num_list[depth]),
            plus, minus, multiply, divide-1)


dfs(1, num_list[0], plus, minus, multiply, divide)
print(maxNum)
print(minNum)
