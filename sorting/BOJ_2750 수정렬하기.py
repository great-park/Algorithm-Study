n = int(input())
num = list()

for _ in range(n):
    num.append(int(input()))

for i in range(n):
    min = i
    for j in range(i+1, n):
        if num[min] > num[j]:
            min = j

    num[i], num[min] = num[min], num[i]

for i in num:
    print(i)
