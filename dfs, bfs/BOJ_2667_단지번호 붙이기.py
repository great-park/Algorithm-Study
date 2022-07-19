import sys
from collections import deque
input = sys.stdin.readline
ans = []

# graph, visited
N = int(input())
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]


# 이동 방향 : 위, 아래, 왼쪽, 오른쪽
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(a, b):
    queue = deque([(a, b)])

    # graph[i][j] == 1인 i,j에서 시작하므로
    graph[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    # visited 대신 graph 좌표를 0으로 바꿔서 solve에서 걸리지 않도록
                    graph[nx][ny] = 0
                    cnt += 1
    if cnt != 0:
        ans.append(cnt)


def solve():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                BFS(i, j)


solve()
print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
