# (0,0) 시작  (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7)
import sys
input = list(sys.stdin.readline().split(' '))
N, M, block_num = int(input[0]), int(input[1]), int(input[2])
ground = [0 for _ in range(N)]

for i in range(N):
    ground[i] = list(map(int, sys.stdin.readline().split(' ')))


leastTime = 1e9

# 3중 for문으로 height로 높이 맞추고, 각 층마다 최소 시간인지 확인후 갱신
for height in range(257):
    fill_up = 0
    dig = 0
    for x in range(N):
        for y in range(M):
            if ground[x][y] < height:
                fill_up += height - ground[x][y]
            else:
                dig += ground[x][y] - height
    if fill_up > dig + block_num:
        continue
    time = 2*dig + fill_up

    if leastTime >= time:
        leastTime = time
        final_height = height

print(leastTime, final_height)
"""
코드에서는 3중 for문을 돌지만 실제로는 최대 높이가 257개(0 포함), 
행렬의 최대 사이즈는 250,000이므로 
256 * 250,000 = 64,250,000 이므로 충분히 1초만에 모든 경우를 계산
"""
