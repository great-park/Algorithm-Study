import sys
from tempfile import tempdir

input = list(sys.stdin.readline().rstrip())
stack = []
# temp로 한 괄호에 대해서 값을 계산
temp = 1
# result에 최종 반영하여 + 구현
result = 0

for i in range(len(input)):
    x = input[i]

    if x == '(':
        temp *= 2
        stack.append(x)
    elif x == '[':
        temp *= 3
        stack.append(x)
    elif x == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if input[i-1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if input[i-1] == '[':
            result += temp
        temp //= 3
        stack.pop()
if stack:
    result = 0
print(result)
