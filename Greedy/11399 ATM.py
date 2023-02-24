from sys import stdin
input = stdin.readline
N = int(input())
time = list(map(int, input().split()))
time.sort()
sum = 0
result = 0
for i in range(N):
    sum += time[i]
    result += sum
print(result)
