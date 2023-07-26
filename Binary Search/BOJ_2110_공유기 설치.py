from sys import stdin
input = stdin.readline
N, C = map(int, input().split())
router = list(int(input()) for _ in range(N))
router.sort()
# 가장 인접한 공유기 간의 거리
start, end = 1, router[-1] - router[0]

while start <= end:
    mid = (start + end) // 2  # 공유기 간 거리
    cnt = 1  # 공유기 개수
    current_coordinate = router[0]

    # 집들의 인덱스로
    for i in range(1, len(router)):
        if router[i] >= current_coordinate + mid:
            cnt += 1
            current_coordinate = router[i]

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)
