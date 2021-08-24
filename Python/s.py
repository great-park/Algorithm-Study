#이진 탐색 알고리즘
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None

    mid = (start_index + end_index) // 2
    if some_list[mid] == element:
        return mid
    elif some_list[mid] < element:
        start_index = mid + 1
        return binary_search(element, some_list, start_index, end_index)
    else:
        end_index = mid - 1
        return binary_search(element, some_list, start_index, end_index)