# counting sort로 풀이 - 인덱스를 값과 매칭시키고, value를 횟수를 저장
import sys

n = int(sys.stdin.readline())
array = [0]*10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for k in range(array[i]):
            print(i)
