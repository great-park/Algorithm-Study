from sys import stdin
input = stdin.readline
N = int(input().rstrip())
rope = []
for i in range(N):
    rope.append(int(input().rstrip()))
rope.sort(reverse=True)
# 20 30 40 => (20,30,40) => 60 // (30,40) => 60 // 40 => 40
# 10 30 70 => (10,30,70) => 30 // (30,70) => 60 // 70 => 70
# 버티는 중량이 큰 로프부터 추가하여 최대 중량을 계산해 간다.

max_weigh = -1e9
rope_num = 0
temp = []
for i in range(N):
    rope_num += 1
    temp.append(rope[i])
    max_weigh = max(max_weigh, rope_num * temp[-1])
print(max_weigh)
