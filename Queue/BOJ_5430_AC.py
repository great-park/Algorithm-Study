import sys
from collections import deque
input = sys.stdin.readline
error_flag = 0


def R(arr):
    arr.reverse()
    return


def D(arr):
    global error_flag
    if len(arr) == 0:
        error_flag = 1
    else:
        arr.popleft()
    return


def solve():
    func = list(input().rstrip())
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    for operator in func:
        if operator == 'R':
            R(arr)
        elif operator == 'D':
            D(arr)

    if error_flag == 1:
        print("error")
    else:
        print("["+",".join(arr)+"]")


T = int(input())
for i in range(T):
    solve()
