from collections import deque
import sys


N = int(sys.stdin.readline())
queue = deque()

while True:
    x = int(sys.stdin.readline())
    if x == -1:
        break
    elif x !=0 and len(queue) < N:
        queue.append(x)
    elif x == 0:
        queue.popleft()
if queue:
    print(*queue)
else:
    print("empty")

# N = int(input())
# data = deque()

# while True:
#     x = int(input())
#     if x == -1:
#         break
#     else:
#         data.append(x)


# buffer = deque()
# while data:
#     current = data.popleft()
#     if current == 0 and buffer:
#         buffer.popleft()

#     elif len(buffer) + 1 > N:
#         continue
#     else:
#         buffer.append(current)


# if len(buffer) == 0:
#     print("empty")
# else:
#     while buffer:
#         print(buffer.popleft(), end=' ')
