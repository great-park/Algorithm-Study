from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    _age, name = input().split()
    age = int(_age)
    data.append((age, name))

# sort
data.sort(key=lambda x: x[0])

for item in data:
    print(item[0], item[1])
