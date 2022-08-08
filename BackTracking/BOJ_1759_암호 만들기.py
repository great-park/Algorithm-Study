from sys import stdin
input = stdin.readline
L, C = map(int, input().split())
pwd = sorted(list(input().split()))
visited = [0]*C
ans = []

# (1) L글자 (2) 최소 1개의 모음 (3) 최소 2개의 자음


def solve(depth):
    if len(ans) == L and checkA(ans):
        print(''.join(map(str, ans)))
        return
    for i in range(depth, C):
        if visited[i] == 0:
            if len(ans) == 0:
                ans.append(pwd[i])
                visited[i] = 1
                solve(depth+1)
                ans.pop()
                visited[i] = 0
            else:
                if ans[-1] < pwd[i]:
                    ans.append(pwd[i])
                    visited[i] = 1
                    solve(depth+1)
                    ans.pop()
                    visited[i] = 0


def checkA(list):
    flag1 = False
    flag2 = False
    cnt = 0
    for x in list:
        if x in ['a', 'e', 'i', 'o', 'u']:
            flag1 = True
        else:
            cnt += 1
    if cnt >= 2:
        flag2 = True
    return flag1 and flag2


solve(0)
