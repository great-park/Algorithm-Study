import sys
from collections import deque
input = sys.stdin.readline

# 범위 계산에 사용할 MAX값 선언 - N,K의 최댓값
MAX = 10**5


def BFS(N, K):
    graph = [0] * (2*MAX + 1)
    queue = deque([N])
    while queue:
        x = queue.popleft()

        # K : 동생 자리
        if x == K:
            print(graph[K])
            return
        # 순간이동 -> 무한 루프 방지를 위해서 순간 이동 시 걸어가는 경우보다 동생과 가까워 질 경우에만 사용
        #    1. 이동 전 조건문에서 graph 범위 확인 필요
        #    2. 이동할 자리의 값이 0인지 확인
        #       만약 0이 아니라면, 이미 "다른 경로"로 해당 자리를 거쳤고,
        #       그 자리 값에 1을 더하는 행위는 곧, 현재의 경로가 최단 경로가 아님을 의미한다.
        if graph[2*x] == 0 and abs(K-2*x) < abs(K-x):
            queue.append(2*x)
            graph[2*x] = graph[x] + 1
        if x + 1 <= MAX and graph[x+1] == 0:
            queue.append(x+1)
            graph[x+1] = graph[x] + 1
        if x - 1 >= 0 and graph[x-1] == 0:
            queue.append(x-1)
            graph[x-1] = graph[x] + 1


N, K = map(int, input().split())
BFS(N, K)
