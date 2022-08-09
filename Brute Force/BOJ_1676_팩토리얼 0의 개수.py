n = int(input())

num = 1
for i in range(1, n+1):
    num *= i
num_list = list(map(int, str(num)))

cnt = 0
for i in range(len(num_list)-1, -1, -1):
    if num_list[i] == 0:
        cnt += 1
    else:
        break
print(cnt)
