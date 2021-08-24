"""
pibot은 리스트 마지막 요소로 지정
리스트 첫번째, b와 i / i와 pibot끼리 비교, i번째가 더 크다면 Big group, 그대로 둠
i번째
"""


def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


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