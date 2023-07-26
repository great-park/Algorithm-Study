from sys import stdin
input = stdin.readline


def solve(k, s, ans, depth):
    if len(ans) == 6:
        print(*ans)  # unpacking
        return

    # (1)중복x (2)오름차순
    for i in range(depth, k):
        if len(ans) == 0:
            ans.append(s[i])
            depth += 1
            solve(k, s, ans, depth)
            ans.pop()
            depth -= 1
        else:
            if s[i] > ans[-1]:
                ans.append(s[i])
                depth += 1
                solve(k, s, ans, depth)
                ans.pop()
                depth -= 1


while True:
    x = list(map(int, input().split()))
    K = x[0]
    S = x[1:]
    if K == 0:
        break
    ans = []
    solve(K, S, ans, 0)
    print()
