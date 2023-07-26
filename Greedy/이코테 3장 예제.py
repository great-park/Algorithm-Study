n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0

while True:

    for i in range(k):
        if m == 0:
            break
        result += data[n-1]
        m -= 1
    if m == 0:
        break
    result += data[n-2]
    m -= 1

print(result)

# ---- ---- ----
n, m = map(int, input().split())
result = 0
save = list()
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    save.append(min_value)

print(max(save))

# ---- ---- ----
n, k = map(int, input().split())
result = 0
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
