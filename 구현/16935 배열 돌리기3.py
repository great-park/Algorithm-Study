from sys import stdin
input = stdin.readline
N, M, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
inst = map(int, input().split())


def solve(x):
    temp = [[0 for _ in range(M)] for _ in range(N)]
    temp2 = [[0 for _ in range(N)] for _ in range(M)]
    if x == 1:
        for i in range(N):
            temp[i] = data[N-1-i]
        return temp

    if x == 2:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][M-1-j]
        return temp

    """
              x
    xixx ->   i
              x
              x

    i, j  =>   N-1-j, i
    """
    if x == 3:
        for i in range(M):
            for j in range(N):
                temp2[i][j] = data[N-1-j][i]
        return temp2

    if x == 4:
        for i in range(M):
            for j in range(N):
                temp2[i][j] = data[j][M-1-i]
        return temp2

    if x == 5:
        for i in range(N//2):
            for j in range(M//2):
                temp[i][j+M//2] = data[i][j]  # 1->2

            for k in range(M//2, M):
                temp[i+N//2][k] = data[i][k]  # 2->3

        for i in range(N//2, N):
            for j in range(M//2):
                temp[i-N//2][k] = data[i][j]  # 4->1

            for k in range(M//2, M):
                temp[i][j-M//2] = data[i][k]
        return temp


for ins in inst:
    data = solve(ins)

for row in data:
    print(*row)
