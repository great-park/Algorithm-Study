from collections import deque

N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
now_x, now_y = 0,0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
shark_size = 2
INF = 1e9

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            now_x,now_y = i,j
            graph[i][j] = 0


def BFS():
    q = deque()
    q.append([now_x, now_y])

    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1 and shark_size >= graph[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1

    return visited

def solve(visited):
    x,y = 0,0
    min_value = INF
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if min_value > visited[i][j]:
                    x,y = i,j
                    min_value = visited[i][j]
    if min_value == INF:
        return False
    else:

        return x,y,min_value



answer = 0
food = 0

while True:
    result = solve(BFS())

    if not result:
        print(answer)
        break
    else:
        now_x, now_y,time = result[0], result[1], result[2]
        graph[now_x][now_y] = 0
        food += 1
        answer += time

    if food >= shark_size:
        shark_size += 1
        food = 0
