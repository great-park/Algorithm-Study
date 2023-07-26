from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

result = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def BFS(x):
    distance = [0] * (N+1)
    visited = [False]*(N+1)
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        a = queue.popleft()
        for adj in graph[a]:
            if not visited[adj]:
                distance[adj] = distance[a] + 1
                visited[adj] = True
                queue.append(adj)

    result.append(sum(distance))


for i in range(1, N+1):
    BFS(i)
print(result.index(min(result))+1)
