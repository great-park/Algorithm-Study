from sys import stdin
input = stdin.readline

S = int(input())

# 무조건 1부터 n까지 차례대로 합: K(n) -> S가 K(n)와 K(n+1) 사이로 오는 구간 찾기

sum = 0
n = 1
while S >= sum:
    sum = (n *(n+1)) // 2
    if S < sum:
        break
    else:
        n += 1

print(n-1)