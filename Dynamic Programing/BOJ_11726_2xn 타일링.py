"""
a1=1, a2=2, a3=3, a4= a3+2 .....

n에 대해서 n-1번째 답에다가 세로타일 하나 붙이는 수 + n-2 번째 답에다가 가로타일 두개 붙이는 수
Dp(n) = Dp(n-1)+Dp(n-2)
"""
n = int(input())
cache = [0]*1001
cache[1] = 1
cache[2] = 2

for i in range(3, 1001):
    cache[i] = cache[i-1]+cache[i-2]

print(cache[n])
