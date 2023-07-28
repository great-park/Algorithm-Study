import sys
input = sys.stdin.readline

N = int(input())
triangle = []

for i in range(N):
    sub = list(map(int, input().split()))
    triangle.append(sub)

for j in range(1, N):
    size = len(triangle[j])
    for i in range(size):
        if i != 0 and i != size-1:
            # print(f'case1 before {j}층, {i} {triangle[j][i]}')
            # print(f'ddd {triangle[j-1][i-1]} vs {triangle[j-1][i]}')
            triangle[j][i] += max(triangle[j-1][i-1], triangle[j-1][i])
            # print(f'case1 after {triangle[j][i]}')
        elif i == 0:
            triangle[j][i] += triangle[j-1][i]
        else:
            # print(f'case2 before {j}층, {i} {triangle[j][i]}')
            # print(f'ddd {triangle[j-1][i-1]}')
            triangle[j][i] += triangle[j-1][i-1]
            # print(f'case2 after {triangle[j][i]}')

print(max(triangle[N-1]))

# 34분