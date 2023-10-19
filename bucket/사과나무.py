from sys import stdin
input = stdin.readline

N = int(input())
hope = list(map(int, input().split()))

def can_satisfy(N, trees):
    # Calculate total height and counts of trees with remainder 1 and 2 when divided by 3
    total_height = sum(trees)
    remainders = [0, 0, 0]
    for height in trees:
        remainders[height % 3] += 1

    r1 = remainders[1]
    r2 = remainders[2]
    
    # If total height is a multiple of 3
    if total_height % 3 == 0:
        if r1 + r2 == N or r1 + r2 == N - 1:
            return "YES"
    else:
        if r1 + r2 == N:
            return "YES"
    return "NO"

print(can_satisfy(N,hope))