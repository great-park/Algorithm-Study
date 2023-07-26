from sys import stdin
from itertools import combinations
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

distance = 1e9

for x in combinations(chicken, m):
    temp = 0
    for hx, hy in home:
        mini = 1e9
        for cx, cy in chicken:
            mini = min(mini, abs(hx-cx)+abs(hy-cy))
        temp += mini
    distance = min(distance, temp)
print(distance)
