import sys
from time import time
N = int(input())
time_table = list()
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append([start, end])
# 시작과 끝이 같은 경우가 있으므로 시작 기준으로 먼저 정렬
# 항상 다음 회의를 고를 때 일찍 끝나는 회의를 고른다
time_table = sorted(time_table, key=lambda x: x[0])
time_table = sorted(time_table, key=lambda x: x[1])

count = 1
ex_room = time_table[0]

for room in time_table[1:]:
    if ex_room[1] <= room[0]:
        count += 1
        ex_room = room
print(count)
