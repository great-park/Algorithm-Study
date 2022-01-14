# def merge(list1, list2):
#     i = 0
#     j = 0
#     merged_list = []
#     while i < len(list1) and j < len(list2):
#         if list1[i] > list2[j]:
#             merged_list.append(list2[j])
#             j += 1
#         else:
#             merged_list.append(list1[i])
#             i += 1
#     if i == len(list1):
#         merged_list += list2[j:]
#     elif j == len(list2):
#         merged_list += list1[i:]
#     return merged_list
#
#
# # 합병 정렬
# def merge_sort(my_list):
#     # base casee
#     if len(my_list) < 2:
#         return my_list
#     left_half = my_list[: (len(my_list) // 2)]
#     right_half = my_list[(len(my_list) // 2):]
#
#     return merge(merge_sort(left_half), merge_sort(right_half))

def merge(list1, list2):
    i=0
    j=0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.appeendv(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i +=1
    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]
    return merged_list

def merge_sort(my_list):
    if len(my_list)<2:
        return my_list
    left_half = my_list[: (len(my_list) //  2)]
    right_half = my_list[(len(my_list) // 2): ]

    return merge(merge_sort(left_half), merge_sort(right_half))


print(merge_sort([4,3,2,5,1,2,5,3,3,2,5,2,65,1,4]))



