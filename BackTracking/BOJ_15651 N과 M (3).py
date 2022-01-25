n, m = list(map(int, input().split()))

ans = []


def dfs():
    if len(ans) == m:  # m개까지 채우고 출력, 이후 백트래킹
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        ans.append(i)
        dfs()
        ans.pop()


dfs()
