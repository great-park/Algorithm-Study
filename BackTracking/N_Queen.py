import sys

n = int(sys.stdin.readline())

cnt = 0


def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):  # abs- 절댓값 함수
        # 수직 체크 or 대각선 체크
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate):
    global cnt
    if current_row == N:  # 여기까지 호출됐다는 것은 퀸의 배치가 완료된 것.
        cnt += 1
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate)
            current_candidate.pop()  # 백트래킹


def solve_n_queens(N):

    DFS(N, 0, [])
    print(cnt)
    return


solve_n_queens(n)
#
"""
promising 조건
1. 같은 열 체크 :  col[i] == col[k]
2. 대각선 체크  :  abs(col[i]-col[k]) == i-k
"""
count = 0


def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i]-col[k]) == (i-k)):
            flag = False
        k += 1
    return flag


def n_queens(i, col):
    global count
    n = len(col) - 1
    if (promising(i, col)):
        if(i == n):
            count += 1
            # print(col[1:n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)


x = int(input())
col = [0] * (x+1)
n_queens(0, col)
print(count)
