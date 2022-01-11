import random


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
    ans = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ans.append(left[l])
            l += 1
        else:
            ans.append(right[r])
            r += 1
    while l < len(left):
        ans.append(left[l])
        l += 1
    while r < len(right):
        ans.append(right[r])
        r += 1
    return ans


data = random.sample(range(100), 10)
print(merge_sort(data))
