n = int(input())

temp = []

for i in range(n):
    a, b = map(int, input().split())
    temp.append((a, b))


def merge_sort(list):

    if(len(list) <= 1):
        return list

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    left2 = merge_sort(left)
    right2 = merge_sort(right)

    return merge(left2, right2)


def merge(left, right):

    i = 0
    j = 0
    sorted_list = []

    while((i < len(left)) & (j < len(right))):
        if(left[i] < right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while(i < len(left)):
        sorted_list.append(left[i])
        i += 1
    while(j < len(right)):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


temp = merge_sort(temp)

for i in range(n):
    print(temp[i][0], end=' ')
    print(temp[i][1])
