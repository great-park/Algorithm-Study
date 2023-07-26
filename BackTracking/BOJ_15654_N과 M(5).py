from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = []


def solve():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if len(ans) == 0:
            ans.append(num[i])
            solve()
            ans.pop()
        else:
            if num[i] not in ans:
                ans.append(num[i])
                solve()
                ans.pop()


solve()
