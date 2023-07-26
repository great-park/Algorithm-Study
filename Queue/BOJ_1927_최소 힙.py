import heapq
from sys import stdin
input = stdin.readline

N = int(input())
heap = []


def pop():
    if len(heap) == 0:
        print(0)
        return
    else:
        print(heapq.heappop(heap))
        return


def push(x):
    heapq.heappush(heap, x)


for i in range(N):
    x = int(input())

    if x == 0:
        pop()
    else:
        push(x)
