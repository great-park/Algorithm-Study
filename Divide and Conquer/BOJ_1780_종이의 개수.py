from sys import stdin
input = stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
minus_one = 0
one = 0
zero = 0


def recursive(x, y, n):
    global minus_one, one, zero

    cur_num = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != cur_num:
                nx = [x, x+n//3, x+2*n//3, x, x+n //
                      3, x+2*n//3, x, x+n//3, x+2*n//3]
                ny = [y, y, y, y+n//3, y+n//3, y+n //
                      3, y+2*n//3, y+2*n//3, y+2*n//3]
                nn = n//3
                for k in range(9):
                    recursive(nx[k], ny[k], nn)
                return
    if cur_num == -1:
        minus_one += 1
        return
    elif cur_num == 0:
        zero += 1
        return
    else:
        one += 1
        return


recursive(0, 0, N)
print(minus_one)
print(zero)
print(one)
