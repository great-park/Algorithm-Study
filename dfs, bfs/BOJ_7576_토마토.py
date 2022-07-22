import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
print(graph)
# dx = [0, 0, 1, -1, 0 ,0]
# dy = [1, -1, 0, 0, 0 ,0]
# dz = [0, 0, 0, 0, 1, -1]
# day = 0
# queue = deque()

# def BFS():
#     while queue:
#         x, y, z = queue.popleft()
#         for i in range(6):
#             nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
#             if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
#                 if graph[nx][ny][nz] == 0:
#                     graph[nz][nx][ny] = graph[z][x][y]+1
#                     queue.append((nx, ny, nz))

#                 elif graph[nx][ny] == 0:
#                     # 익은 토마토의 인접한 토마토는 다음 날 익는다. 아직 방문 안 함.
#                     graph[nx][ny] = 1

#     day += 1


# for i in range(M):
#     for j in range(N*H):
