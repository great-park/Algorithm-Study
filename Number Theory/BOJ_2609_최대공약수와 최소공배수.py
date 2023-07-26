import sys
input = sys.stdin.readline

M, N = map(int, input().split())

# 유클리드 호제법
# +) m * n = 최대공약수(GCD) * 최소공배수(LCM)

def mod(m, n):
  if n == 0: return m
  if (m % n == 0): return n
  else: return mod(n, m % n)

gcd = mod(M,N)
lcm = int(M*N/gcd)

print(gcd)
print(lcm)
