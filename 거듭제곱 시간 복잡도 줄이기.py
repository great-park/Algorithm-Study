# 일반 반복문 사용 - 시간 복잡도 : O(y)
def power_no(x, y):
    total = 1

    # x를 y번 곱해 준다
    for i in range(y):
        total *= x

    return total


# 재귀 사용 - 시간 복잡도 : O(logy)
def power(x, y):
    # Base Case
    if y == 0:
        return 1
    # Recursive Case
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    elif y == 1:
        return x
    else:
        return power(x, (y // 2) + 1) * power(x, (y // 2))

# 재귀 사용 2
def power2(x, y):
    if y == 0:
        return 1

    # 계산을 한 번만 하기 위해서 변수에 저장
    subresult = power(x, y // 2)

    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))