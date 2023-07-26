from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
lesson = list(map(int, input().split()))
# 1개의 블루레이에 최소 1개의 강의가, 최대 모든 강의가 들어감
start, end = max(lesson), sum(lesson)

while start <= end:
    mid = (start + end) // 2  # 블루레이 길이
    size = 0  # 현재 블루레이에 들어온 강의의 길이
    cnt = 0  # 블루레이 개수

    for i in range(N):
        if size + lesson[i] > mid:  # 블루레이에 더 담을 수 없을 떄
            cnt += 1
            size = 0  # 다음 블루레이로 넘기기
        size += lesson[i]

    cnt += 1 if size else 0  # 마지막 블루레이에 강의 들었는지 확인

    # 블루레이 수를 늘려야 한다면 -> 길이를 줄이기
    if cnt <= M:
        end = mid - 1
    # 블루레이 수를 줄여야 한다면 -> 길이를 늘리기
    else:
        start = mid + 1

print(start)
