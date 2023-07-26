# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)
    p = b

    return p


# 퀵 정렬
def quicksort(my_list, start, end):
    if end - start < 1:
        return
    pivot = partition(my_list, start, end)

    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)



