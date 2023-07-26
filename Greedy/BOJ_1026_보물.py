from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름 차순으로 정렬, B는 내림 차순으로 정렬
A.sort()
B.sort(reverse=True)
result = 0

for i in range(len(A)):
    result += A[i] * B[i]

print(result)
