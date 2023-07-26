import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2

mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)


"""
코드 해석

zip(stat, zip(*stat)) 은 stat의 원소(= 행) 과 zip(*stat)(=열) 을 차례대로 뱉어내므로 k번째 행과 열을 뱉어줍니다.

즉, newstat은 [1번째 행과 열의 합, 2번째 행과 열의 합, ... N번째 행과 열의 합] 으로 된 list 입니다.

allstat은 newtstat의 원소를 다 더한 다음 2로 나눴으므로 전체 행렬의 원소의 합이 됩니다. (2로 나눈 것은 행렬의 각 원소가 2번씩 더해지기 때문입니다)

따라서 전체 행렬의 합은 allstat이 되고, 초록색 행/열의 합은 newstat의 원소에서 N//2 개를 뽑아서 더해주면 됩니다. N//2개를 뽑을때 itertools.combinations를 사용한 것이구요.

(코드에서는 3번째 줄에 이미 2로 나눠서 cb(newstat[:-1], N//2) 가 아닌 cb(newstat[:-1], N) 로 되어있습니다)

즉, abs(allstat - sum(l)) 이 부분이  전체 행렬 합 - 초록색 행/열의 합 이 됩니다.

그리고 cb(newstat, N)이 아니라 cb(newstat[:-1], N) 으로 되어있는 이유는 겹치는 경우를 빼 주려고 N개를 뽑을 때 마지막 선수는 제외하고 뽑은 것 입니다.

(마지막 선수는 항상 B팀에 속한다 생각해도 답은 바뀌지 않으니까요)
"""
stat = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

print(*stat)
# stat의 행
# [1, 2, 3, 4] [4, 5, 6, 7] [8, 9, 10, 11] [12, 13, 14, 15]


# stat의 열
for i in zip(*stat):
    print(i)
# (1, 4, 8, 12)
# (2, 5, 9, 13)
# (3, 6, 10, 14)
# (4, 7, 11, 15)


# stat의 k번째 행과 열
for i, j in zip(stat, zip(*stat)):
    print("i: {}, j: {}".format(i, j))
# i: [1, 2, 3, 4],     j: (1, 4, 8, 12)
# i: [4, 5, 6, 7],     j: (2, 5, 9, 13)
# i: [8, 9, 10, 11],   j: (3, 6, 10, 14)
# i: [12, 13, 14, 15], j: (4, 7, 11, 15)
