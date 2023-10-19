from sys import stdin
from collections import deque
input = stdin.readline

N, M, V = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1



def DFS(start):
    return 1

def BFS(start):
    queue = deque()
    visited = [False for _ in range(N+1)]
    queue.append(start)
    visited[start] = True
    print(start, end=' ')

    while queue:
        node = queue.popleft()
        for i in (1,N+1):
            if not visited[i] and graph[node][i] == 1:
                queue.append(i)
                visited[i] = True
                print(node, end=' ')


BFS(V)