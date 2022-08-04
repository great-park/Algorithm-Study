from ast import operator
from sys import stdin
input = stdin.readline

M = int(input())
bit = 0
for _ in range(M):
    temp = list(input().split())

    if len(temp) == 1:
        if temp[0] == 'all':
            bit = (1 << 20) - 1
        else:
            bit = 0
    else:
        operator, num = temp[0], int(temp[1]) - 1

        if operator == 'add':
            # num 자리만 1로 만들고 나머지는 0, 이것과 or 연산
            # => 기존 bit에서 num 자리만 1로 바뀐다
            bit |= (1 << num)
        elif operator == 'remove':
            # num 자리만 0으로 만들고 나머지는 1, 이것과 and 연산
            # => 기존 bit에서 num 자리만 0으로 바뀐다
            bit &= ~(1 << num)
        elif operator == 'check':
            # num 자리만 1로 만들고 나머지는 0, 이것과 bit를 and 연산
            # => bit의 num 자리가 0 이면 0 출력, 1이면 1 출력
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif operator == 'toggle':
            # num 자리만 1로 만들고 나머지는 0, 이것과 bit를 xor 연산
            # => bit에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
            bit = bit ^ (1 << num)
