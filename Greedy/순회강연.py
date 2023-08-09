# from sys import stdin
# from collections import deque

# input = stdin.readline
# N = int(input())
# schedule = list()
# max_day = 0
# for i in range(N):
#     cost, day = map(int, input().split())
#     max_day = max(max_day, day)
#     schedule.append([cost, day])
# schedule.sort(key= lambda x : [-x[0], x[1]])

# print(schedule)

# answer = 0

# day_count = 1
# for item in schedule:
#     if item[1] >= day_count:
#         answer += item[0]
#     day_count += 1




# 잘못된 방향임    
# schedule.sort(key= lambda x: [x[1], -x[0]]) # 강의 날짜순으로 대학 정렬, 각 날짜에서는 금액이 큰 순으로 정렬

# day_list = deque()
# for one_day_sch in schedule:
#     day = one_day_sch[1]
#     if day not in day_list:
#         day_list.append(day)

# day_pointer = day_list.popleft()
# new_schedule = list()

# # 강의 시간은 무조건 하루이기 때문에 각 날짜에는 무조건 금액을 많이 주는 대학을 고르면 된다. 
# for i in range(len(schedule)):
#     if schedule[i][1] == day_pointer:
#         new_schedule.append(schedule[i])
#         if len(day_list) != 0:
#             day_pointer = day_list.popleft()
#         else:
#             day_pointer += 1

# answer = 0
# MAX = 100000001
# dp = [0] * (max_day+1) # i번째 날에 벌 수 있는 최대 금액


# 답지
import heapq

N=int(input())
schedules=[]
for i in range(N):
  schedules.append(list(map(int, input().split())))

schedules.sort(key=lambda x: (x[1]))

lession_list=[]

for schedule in schedules:
  heapq.heappush(lession_list, schedule[0])
  if (len(lession_list) > schedule[1]):
    heapq.heappop(lession_list)

print(sum(lession_list))

# 실패