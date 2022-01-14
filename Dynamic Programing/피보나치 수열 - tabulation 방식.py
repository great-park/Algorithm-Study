def fib_tab(n):
    cache=[]
    for i in range(1,n+1): #1부터n까지
        if i <3: # i= 1,2
            cache.append(1)
        else:    #i번쨰(3이상) -> cache[i-2] + cache[i-3]// i가 1부터 시작하므로,,
            cache.append( cache[i-2] + cache[i-3] )
    #반복문 결과 인덱스 0부터 n-1번까지 피보나치수 리스트에 정렬
    return cache[n-1]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))