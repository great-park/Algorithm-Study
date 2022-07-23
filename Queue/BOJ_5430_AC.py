import sys
from collections import deque
input = sys.stdin.readline
error_flag = 0
R_num = 0


def R(arr):
    arr.reverse()
    return


def D(arr):
    global error_flag
    if len(arr) == 0 or arr == deque(['']):
        error_flag = 1
    # 짝수번 뒤집었기 때문에 뒤에서 제거
    elif R_num % 2 == 0:
        arr.popleft()
    # 홀수번 뒤집었기 때문에 앞에서 제거
    else:
        arr.pop()
    return


def solve():
    global error_flag
    global R_num
    error_flag = 0
    R_num = 0
    p = list(input().rstrip())
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    for operator in p:
        if operator == 'R':
            R_num += 1
        elif operator == 'D':
            D(arr)
    if error_flag == 1:
        print("error")
    elif R_num % 2 == 0:
        print("["+",".join(arr)+"]")
    else:
        R(arr)
        print("["+",".join(arr)+"]")


T = int(input())
for i in range(T):
    solve()
