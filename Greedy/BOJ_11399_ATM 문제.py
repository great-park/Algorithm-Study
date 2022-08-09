import sys
N = int(input())
time_list = list(map(int, input().split()))
# 가장 짧게 걸리는 사람부터 인출하도록 정렬
time_list.sort()
total_time = 0

for time in time_list:
    total_time += time * N
    N -= 1
print(total_time)
