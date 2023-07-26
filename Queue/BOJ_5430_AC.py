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

#from sys import stdin
# input = stdin.readline

# def solve():

#     for _ in range(int(input())):
#         # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
#         p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

#         n = int(input())
#         arr = input()[1:-2].split(',')
#         # [left, right) 가 출력된다
#         left, right = sum(p[::2]), n - sum(p[1::2])

#         if left <= right:
#             # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
#             arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
#             print(f"[{','.join(arr)}]")
#         else:
#             print('error')


# if __name__ == '__main__':
#     solve()
