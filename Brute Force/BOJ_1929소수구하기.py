x, y = map(int, input().split())

a = [True] * (y+1)
for i in range(2, int((y+1)**0.5)+1):
    if a[i]:
        for j in range(2*i, y+1, i):
            a[j] = False

for i in range(x, y+1):
    if i > 1 and a[i] == True:
        print(i)
