# from sys import stdin
# input = stdin.readline
# N = int(input())
# time = list(map(int, input().split()))
# time.sort()
# sum = 0
# result = 0
# for i in range(N):
#     sum += time[i]
#     result += sum
# print(result)
from sys import stdin
input = stdin.readline
N = int(input())
time = list(map(int, input().split()))
time.sort()
res = 0
for id, value in enumerate(time):
    if id == 0:
        res += value
    else:
        time[id] = value + time[id-1]
print(sum(time))
