from sys import stdin
input = stdin.readline

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]
start, end = 1, max(LAN)

while start <= end:
    mid = (start + end)//2  # 랜선 분할 단위
    num = 0  # 랜선 개수

    for i in LAN:
        num += i//mid  # 각 랜선들을 분할 시 나오는 개수

    if num >= N:  # 필요한 양보다 더 많이 분할된 경우
        start = mid + 1  # 이분 탐색. mid 이하의 값은 필요없다.
    else:
        end = mid - 1  # 이분 탐색. mid 이상의 값은 필요없다.
print(end)
