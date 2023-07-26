n = int(input())

for i in range(n):
    x = int(input())
    cache = [0]*101
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    cache[4] = 2
    cache[5] = 2

    for i in range(6, x+1):
        cache[i] = cache[i-1] + cache[i-5]
    print(cache[x])
