from sys import stdin
input = stdin.readline
N = int(input())
solution = sorted(list(map(int, input().split())))

start, end = 0, N-1
ans = abs(solution[start]+solution[end])
final = [solution[start], solution[end]]

while start < end:
    left = solution[start]
    right = solution[end]

    sum = left + right

    if abs(sum) < ans:
        ans = abs(sum)
        final = [left, right]
        if ans == 0:
            break

    if sum < 0:
        start += 1  # 합이 음수면 0에 가까워지기 위해 start + 1
    else:
        end -= 1  # 합이 양수면 end - 1
print(final[0], final[1])
