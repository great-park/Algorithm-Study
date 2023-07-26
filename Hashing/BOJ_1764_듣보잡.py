from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
hash = set()
for i in range(N):
    people = input().rstrip()
    hash.add(people)

ans = list()
for i in range(M):
    people = input().rstrip()
    if people in hash:
        ans.append(people)


print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])
