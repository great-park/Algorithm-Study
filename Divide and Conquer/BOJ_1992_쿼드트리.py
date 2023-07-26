from sys import stdin
input = stdin.readline
N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
ans = ""


def recursive(x, y, n):
    global ans, N
    cur_value = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != cur_value:
                ans += "("
                # 숫자가 안 맞음
                recursive(x,      y,      n//2)
                recursive(x,      y+n//2, n//2)
                recursive(x+n//2, y,      n//2)
                recursive(x+n//2, y+n//2, n//2)
                ans += ")"
                return

    # 숫자가 다 맞음
    if cur_value == 0:
        ans += "0"
    else:
        ans += "1"
    return


recursive(0, 0, N)
print(ans)
