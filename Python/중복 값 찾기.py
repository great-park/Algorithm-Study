# (N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있습니다. 그렇다면 어떤 수는 꼭 한 번은 반복되겠지요.
#
# 예를 들어 [1, 3, 4, 2, 5, 4]와 같은 리스트 있을 수도 있고, [1, 1, 1, 6, 2, 2, 3]과 같은 리스트가 있을 수도 있습니다. (몇 개의 수가 여러 번 중복되어 있을 수도 있습니다.)
#
# 이런 리스트에서 반복되는 요소를 찾아내려고 합니다.
#
# 중복되는 어떠한 수 ‘하나’만 찾아내도 됩니다. 즉 [1, 1, 1, 6, 2, 2, 3] 예시에서 1, 2를 모두 리턴하지 않고, 1 또는 2 하나만 리턴하게 하면 됩니다.
#
# 중복되는 수를 찾는 시간 효율적인 함수를 설계해보세요.

#1. Brute Force 방법 : O(n^2)
def find_same_number(some_list):
    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            if some_list[i] == some_list[j]:
                return some_list[i]

#2. 이미 나온 요소 저장 : O(n)
def find_same_number2(some_list):
    # 이미 나온 요소를 저장시켜줄 사전
    elements = {}

    for i in some_list:
        if i in elements:
            return i
        elements[i] = True

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))