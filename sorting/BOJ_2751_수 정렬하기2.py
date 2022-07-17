import sys


def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = int(len(data)/2)
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


def merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result


input = sys.stdin.readline
N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

for i in merge_sort(num):
    print(i)
