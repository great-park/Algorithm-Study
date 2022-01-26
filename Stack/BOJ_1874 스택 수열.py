N = int(input())
data = [0 for _ in range(N)]
for i in range(N):
    data[i] = int(input())
ans = list()
ans.append(1)

op = list()
op.append('+')

success = True


def sol():
    pointer = 1
    global success

    for num in data:
        while num > pointer:
            op.append('+')
            pointer += 1
            ans.append(pointer)

        if num == ans[-1]:
            op.append('-')
            ans.pop()
    # 성공하면 무조건 한 번 넣었다가 빼므로, 2N만큼 OP가 찰 것
    if len(op) != 2*N:
        success = False


sol()
if success:
    for operator in op:
        print(operator)
else:
    print("NO")


""" --------------------------------------------
    다른 사람 답안
    --------------------------------------------
"""
n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))  # 한 줄씩 출력
