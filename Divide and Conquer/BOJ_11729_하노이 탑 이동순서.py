n = int(input())
ans = []
cnt = 0


def move(num_disks, start, end):
    global cnt
    cnt += 1
    ans.append([start, end])


def hanoi(num_disks, start, end):

    if num_disks == 0:
        return

    other = 6 - start - end
    # 가장 큰 원판빼고 나머지 다른 쪽으로 옮기기
    hanoi(num_disks-1, start, other)
    move(num_disks, start, end)
    hanoi(num_disks-1, other, end)


hanoi(n, 1, 3)
print(cnt)
for i in range(cnt):
    print(ans[i][0], ans[i][1])
