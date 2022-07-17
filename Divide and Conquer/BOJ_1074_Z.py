# z 하나는 4개의 점으로 구성
# 다음 단계의 큰 Z를 구할 때는 작은 z 하나를 점으로 보자
# 그러면 재귀적으로 분할 정복이 가능하다.
# r,c가 2배씩 증가할 때, cnt는 4배씩 증가
# 주어진 좌표에서 가장 가까운 2의 배수의 r,c를 찾는다.
# z모양으로 움직이기 때문에 딱 그 차이만큼 cnt가 증가한다.

# 풀이 실패. 코드 가져옴 : https://ggasoon2.tistory.com/11?category=972261
# 1번 풀이
def fun(N, r, c):
    if N == 0:
        return 0
    return 2*(r % 2)+(c % 2) + 4*fun(N-1, int(r/2), int(c/2))


N, r, c = map(int, input().split())
print(fun(N, r, c))


# # 2번 풀이 - 실패
# def solve(n, x, y):
#     global result
#     if n == 2:
#         if x == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x == X and y+1 == Y:
#             print(result)
#             return
#         result += 1
#         if x+1 == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x+1 == X and y+1 == Y:
#             print(result)
#             return
#         result += 1
#         return
#     solve(n/2, x, y)
#     solve(n/2, x, y + n/2)
#     solve(n/2, x + n/2, y)
#     solve(n/2, x + n/2, y + n/2)


# result = 0
# N2, X, Y = map(int, input().split(' '))
# solve(2**N2, 0, 0)
