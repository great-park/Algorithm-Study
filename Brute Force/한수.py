z = int(input())
cnt = 0

for x in range(1, z+1):
    x_list = []
    d_list = []
    check = 1

    x_list = list(map(int, str(x)))

    for i in range(len(x_list) - 1):
        d = x_list[i] - x_list[i + 1]
        d_list.append(d)
    for j in range(len(d_list)):
        if d_list[j] != d:
            check = 0
            break

    if check == 1:
        cnt +=1
print(cnt)
