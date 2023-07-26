from sys import stdin
input = stdin.readline
N = int(input())
num = list(map(int, input().split()))
memorization = [0]

for x in num:
    # 가장 오른쪽에 저장
    if memorization[-1] < x:
        memorization.append(x)
    else:
        # 자리 찾기 - 이분 탐색
        start = 0
        end = len(memorization)

        while start < end:
            mid = (start+end)//2

            if memorization[mid] < x:
                start = mid + 1
            else:
                end = mid
        memorization[end] = x
print(len(memorization)-1)
