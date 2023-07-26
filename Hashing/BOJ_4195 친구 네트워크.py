# 그래프 사용
# union
# set 사용
test_case = int(input())


def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])  # 재귀적으로 부모 찾기
    return parent[x]


def union(x, y):  # 왼쪽을 부모로 만들기
    # 부모 찾기
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]
        number[y] = number[x]


for _ in range(test_case):
    parent = dict()
    number = dict()

    f_num = int(input())

    for _ in range(f_num):
        a, b = input().split(' ')

        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)]) 
