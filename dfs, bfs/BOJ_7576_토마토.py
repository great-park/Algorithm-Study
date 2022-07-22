import sys
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()


def BFS():
    while queue:
