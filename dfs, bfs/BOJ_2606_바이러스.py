# from collections import deque
# from re import T
# from sys import stdin
# input = stdin.readline

# N = int(input())
# com_num = int(input())
# graph = list([] for _ in range(N+1))
# visited = [False] * (N+1)
# cnt = 0

# for i in range(com_num):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)


# def DFS(start):
#     global cnt
#     stack = deque([start])

#     while stack:
#         x = stack.pop()
#         visited[x] = True

#         for node in graph[x]:
#             if not visited[node]:
#                 visited[node] = True
#                 stack.append(node)
#                 cnt += 1


# def BFS(start):
#     global cnt
#     queue = deque([start])

#     while queue:
#         x = queue.popleft()
#         visited[x] = True

#         for node in graph[x]:
#             if not visited[node]:
#                 visited[node] = True
#                 queue.append(node)
#                 cnt += 1


# # BFS(1)
# DFS(1)
# print(cnt)

from sys import stdin
from collections import deque
input = stdin.readline
N = int(input())
K = int(input())
graph = [[] for _ in range(N+1)]
for i in range(K):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False]*(N+1)
cnt = 0


def BFS(x):
    global cnt
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True
                cnt += 1


BFS(1)
print(cnt)
