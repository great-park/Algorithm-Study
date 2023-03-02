from sys import stdin
from collections import deque
input = stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

ans = [0]*(N+1)


def BFS():
    queue = deque()
    queue.append(1)  # 루트

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if ans[child] == 0:
                ans[child] = node
                queue.append(child)


BFS()
print(*ans[2:])
