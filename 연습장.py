n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

max_value = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = data[i]+data[j]+data[k]
            if sum <= m:
                max_value = max(max_value, sum)
print(max_value)
