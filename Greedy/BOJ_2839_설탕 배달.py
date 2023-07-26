n = int(input())
cnt = 0
# greedy : 5로 나누어 떨어질 경우 전부 5로 사용
while n >= 3:
    if n % 5 == 0:  # 5의 배수
        cnt += (n//5)
        n = 0
        break
    n -= 3
    cnt += 1

if not n:
    print(cnt)
else:
    print(-1)
