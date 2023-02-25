num = list(map(int, input().rstrip()))
num.sort(reverse=True)
# 30으로 나누어 떨어지기 위해서는
# (1) 마지막이 0 (2) 나머지 숫자들의 합이 3의 배수
sum = 0
for i in num:
    sum += i
if sum % 3 == 0 and num[-1] == 0:
    print(''.join(map(str, num)))
else:
    print(-1)
