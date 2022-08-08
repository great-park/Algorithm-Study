from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 1은 집, 2는 치킨집
homes = []
chickens = []
# 추가한 치킨집
ans = []
# 방문 목록
visited = [[0]*N for _ in range(N)]
# 거리 목록
distance_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))


def getDistance():
    x = 0
    # 집을 기준으로 치킨 거리를 계산. 한 집에 대해 여러 개의 치킨집 거리 계산
    for hx, hy in homes:
        distance = 1e9
        for id, (cx, cy) in ans:
            distance = min(distance, abs(hx-cx)+abs(hy-cy))
        x += distance
    distance_list.append(x)


# 치킨집을 하나씩 추가하면서 M개가 되었을 때 추가
def solve(depth):
    if depth == M:
        getDistance()
        return

    for id, (cx, cy) in enumerate(chickens):
        if not visited[cx][cy]:
            # 이전 solve에서 검토한 치킨 집은 건너뛰어도 됨
            if ans and id < ans[-1][0]:
                continue
            visited[cx][cy] = 1
            ans.append((id, (cx, cy)))
            solve(depth+1)
            visited[cx][cy] = 0
            ans.pop()


solve(0)
print(min(distance_list))
