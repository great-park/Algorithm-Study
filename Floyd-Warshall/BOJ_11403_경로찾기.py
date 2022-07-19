import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# Floyd-Warshall - 모든 정점에 대한 경로 계산
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


# 출력
for row in graph:
    for col in row:
        print(col, end=" ")
    print()


# DFS
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]


def dfs(x):
    # x번째 정점과 나머지 정점들 비교
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


for i in range(n):
    # i번째 정점
    dfs(i)
    # DFS 종료 후, 인접 행렬을 돌면서 출력
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()  # 다음 정점 출력으로 넘어가기
    # 초기화
    visited = [0 for _ in range(n)]
