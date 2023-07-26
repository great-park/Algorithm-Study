n = int(input())

cache = [0]*1001
cache[1] = 1
cache[2] = 3

# (i-1)에서 1X2 블럭  + (i-2)에서 2X1 블럭 2개 and 2x2 블럭 1개
for i in range(3, 1001):
    cache[i] = cache[i-1] + 2*cache[i-2]

print(cache[n] % 10007)
