n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)


def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False  # Back_Tracking


solve(0)
print(ans)

""" i는 row, j는 column.
인덱스 (x,y)에서 1. 세로줄의 열 = y  2. 대각선 / = x+y  3. 대각선 | = x-y+n-1
"""
