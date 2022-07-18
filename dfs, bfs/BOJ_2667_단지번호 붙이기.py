import sys
from collections import deque
input = sys.stdin.readline
ans = []

# graph, visited
N = int(input())
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# (0,0)에서 시작하므로
visited[0][0] = 1

# 이동 방향 : 위, 아래, 왼쪽, 오른쪽
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# DFS -> 묶이는 단지 내 1의 개수를 count하여 ans에 append한다.


def BFS(a, b):
    queue = deque([(a, b)])
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if graph[nx][ny] == 1:
                        queue.append((nx, ny))
                        cnt += 1
    if cnt != 0:
        ans.append(cnt)
    return x, y  # 마지막 x,y


# visited가 1인 구역을 제외하고 BFS를 실시한다. 이때 graph[][] = 1인 지점을 만나면 DFS()실행
def solve():
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(i, j)
    return


solve()
print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
