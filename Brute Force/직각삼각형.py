import sys

while True:
    edge = list(map(int, sys.stdin.readline().split()))
    edge.sort()
    if sum(edge) == 0:
        break
    elif edge[0]**2 + edge[1]**2 == edge[2]**2:
        print("right")
    else:
        print("wrong")
