from collections import deque
N, K = map(int, input().split())
queue = deque()
answer = []
for i in range(1, N+1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())

    answer.append(queue.popleft())

print("<", end='')

for i in range(N-1):
    print(str(answer[i])+", ", end='')
print(answer[N-1], end='')

print(">")
