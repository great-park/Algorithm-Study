import sys

n = int(sys.stdin.readline())
list_first = sys.stdin.readline().split()
m = int(sys.stdin.readline())
list_second = sys.stdin.readline().split()


def binary_search(value, start, end):

    mid = (start + end)//2

    if start > end:
        return False

    if list_first[mid] > value:
        return binary_search(value, start, mid-1)
    elif list_first[mid] < value:
        return binary_search(value, mid+1, end)
    else:
        return True


# 이진 탐색을 위해 정렬 O(nlogn)
list_first.sort()

# while len(list_second) != 0:
#     search_value = list_second[0]
#     print(binary_search(list_first, search_value))
#     list_second = list_second[1:]

for item in list_second:
    if binary_search(item, 0, n-1):
        print(1)
    else:
        print(0)
