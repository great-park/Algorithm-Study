# 주어진 리스트에서 합이 가장 큰 범위를 찾고 그 값을 리턴
# Brute Force 방식
def sublist_max(profits):
    save_list = []
    for i in range(0, len(profits)):
        temp = profits[i]

        if i == (len(profits) - 1):
            save_list.append(profits[i])
        else:
            for j in range(i + 1, len(profits)):
                temp += profits[j]
                save_list.append(temp)
    return max(save_list)


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))


def sublist_max2(profits):
    max_profit = profits[0]  # 최대 수익

    for i in range(len(profits)):
        # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
        total = 0

        for j in range(i, len(profits)):
            # i부터 j까지 수익의 합을 계산
            total += profits[j]

            # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
            max_profit = max(max_profit, total)

    return max_profit

print(sublist_max2([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max2([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max2([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))