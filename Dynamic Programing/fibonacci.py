def fibo(num):
    cache = [0 for i in range(0, num+1)]
    cache[0] = 0
    cache[1] = 1
    for j in range(2, num+1):
        cache[j] = cache[j-1]+cache[j-2]
    return cache[num]


print(fibo(10))
