from sys import stdin
input = stdin.readline
N = int(input())  # 2의 배수
"""
초기 : 하얀색 = n*n개, 파란색 = 0개

파란색 - 위치에 따라서 하얀색 색종이 갯수가 달라짐
1 4 8 16 32 64 128
"""
graph = [list(map(int, input().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0


def recursive(x, y, n):
    global white_cnt, blue_cnt

    init_color = graph[x][y]

    # 현재의 사각형 내에서 색이 모두 같은지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != init_color:
                # 색이 모두 같지 않으면 => 사각형 형성 x
                # 구역을 나누어 다시 탐색
                recursive(x,      y,      n//2)
                recursive(x,      y+n//2, n//2)
                recursive(x+n//2, y,      n//2)
                recursive(x+n//2, y+n//2, n//2)

                return
    # 색이 모두 같다면 사각형 추가
    if init_color == 0:
        white_cnt += 1
        return
    else:
        blue_cnt += 1
        return


recursive(0, 0, N)
print(white_cnt)
print(blue_cnt)
