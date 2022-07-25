import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def deque_sort(queue):
    return deque(sorted(queue))


def solve():
    queue = deque()
    k = int(input())
    for _ in range(k):
        operator, value = input().split()
        value = int(value)
        if operator == 'I':
            queue.append(value)
            queue = deque_sort(queue)
        else:
            if len(queue) == 0:
                continue
            elif value == 1:
                queue.pop()
            else:
                queue.popleft()
    if len(queue) == 0:
        print('empty')
    else:
        max_value = max(queue)
        min_value = min(queue)
        print(max_value, min_value)


for _ in range(T):
    solve()
