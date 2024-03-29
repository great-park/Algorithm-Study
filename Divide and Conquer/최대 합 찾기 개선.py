def sublist_max(profits, start, end):
    # 범위에 하나의 항목밖에 없으면, 그 항목을 리턴한다
    if start == end:
        return profits[start]
    mid = (start + end) // 2

    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    return max(max_left, max_right, max_cross)

# 리스트 만들고 요소 합치기
def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2

    temp_left = []
    sum_left = profits[mid]
    temp_left.append(profits[mid])
    for i in range(mid - 1, start - 1, -1):
        sum_left += profits[i]
        temp_left.append(sum_left)
    find_index_left = temp_left.index(max(temp_left))

    temp_right = []
    sum_right = profits[mid + 1]
    temp_right.append(profits[mid + 1])
    for j in range(mid + 2, end + 1):
        sum_right += profits[j]
        temp_right.append(sum_right)
    find_index_right = temp_right.index(max(temp_right))

    max_crossing_sum_list = profits[(mid - find_index_left): (mid + 1 + find_index_right) + 1]
    return sum(max_crossing_sum_list)
#바로 합 구하기
def max_crossing_sum2(profits, start, end):
    mid = (start + end) // 2      # 중간 인덱스

    '''
    왼쪽에서의 가장 큰 수익 계산
    인덱스 mid부터 인덱스 0까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    left_sum = 0                  # 왼쪽 누적 수익
    left_max = profits[mid]       # 왼쪽 최고 수익; 왼쪽 반 중 가장 오른쪽 값으로 초기화

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    '''
    오른쪽에서의 가장 큰 수익 계산
    인덱스 mid+1부터 인덱스 end까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    right_sum = 0                 # 오른쪽 누적 수익
    right_max = profits[mid + 1]  # 오른쪽 최고 수익; 오른쪽 반 중 가장 왼쪽 값으로 초기화

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))