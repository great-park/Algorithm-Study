import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split(" "))

print("<", end='')

queue = deque()
for i in range(1, N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    if(len(queue) == 1):
        print(queue.popleft(), end='>')
    else:
        print(queue.popleft(), end=', ')
