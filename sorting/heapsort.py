def max_heapify(a,i, size):
    largest = i
    left = 2*i +1
    right = 2*i +2

    if(left < size and a[left] > a[largest]):
        largest = left
    if(right < size and a[right] > a[largest]):
        largest = right

    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        max_heapify(a,largest,size)

def heap_sort(a):
    length = len(a)
    for i in range(length//2 -1 , -1, -1):
        max_heapify(a,i,length)

    for i in range(length-1,0,-1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a,0,i)
    return a

n = input()
n=int(n)
list_1 =[]
for i in range(n):
    list_1.append(input())

x = heap_sort(list_1)

for i in range(n):
    print(x[i])

