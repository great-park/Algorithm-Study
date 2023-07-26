from sys import stdin
input = stdin.readline
N, M = map(int, input().split())

name_hash = {}
index_hash = {}
for i in range(1, N+1):
    name = input().rstrip()
    name_hash[name] = i
    index_hash[i] = name

# 찾기
for i in range(M):
    x = input().rstrip()
    try:
        # 인덱스로 찾기
        x = int(x)
        print(index_hash[x])
    except:
        # 이름으로 찾기
        print(name_hash[x])
