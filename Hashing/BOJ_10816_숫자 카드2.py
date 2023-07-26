from sys import stdin
input = stdin.readline
N = int(input())
card = map(int, input().split())
M = int(input())
num = map(int, input().split())

hash = {}
for x in card:
    if x in hash:
        hash[x] += 1
    else:
        hash[x] = 1

print(' '.join(str(hash[i]) if i in hash else '0' for i in num))

# from sys import stdin
# input = stdin.readline
# N = int(input())
# MAX = 20000001
# # 리스트의 인덱스 자체를 카드 번호로 사용, 값에는 갯수를 담는다.
# card = list(map(int, input().split()))
# hash = list(0 for _ in range(MAX))
# for i in range(0, N):
#     hash[card[i]] += 1
# M = int(input())
# num = list(map(int, input().split()))

# for i in num:
#     print(hash[i], end=' ')
