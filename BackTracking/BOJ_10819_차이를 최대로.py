from sys import stdin
input = stdin.readline
N = int(input())
num = list(map(int, input().split()))

candidate = []
order = []


def solve(depth):
    if depth == N:
        candidate.append(
            sum(abs(num[order[i + 1]] - num[order[i]]) for i in range(N - 1)))
        return

    for x in range(N):
        if x not in order:
            order.append(x)
            solve(depth+1)
            order.pop()


solve(0)
print(max(candidate))
