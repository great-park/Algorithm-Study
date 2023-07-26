from itertools import permutations
# 순열 기능 제공
import sys

N = int(input())
input = sys.stdin.readline
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
operators = list()
# plus, minus, multiply, divide = operator_list[0], operator_list[1], operator_list[2], operator_list[3]
# for _ in range(plus):
#     operator.append('+')
# for _ in range(minus):
#     operator.append('-')
# for _ in range(multiply):
#     operator.append("*")
# for _ in range(divide):
#     operator.append('/')
operator_sample = ['+', '-', '*', '/']
for i in range(4):
    for j in range(operator_list[i]):
        operators.append(operator_sample[i])

operators = list(set(permutations(operators, len(operators))))

ans = list()

for operator in operators:
    result = num_list[0]

    for j in range(N-1):
        if operator[j] == '+':
            result += num_list[j+1]
        elif operator[j] == '-':
            result -= num_list[j+1]
        elif operator[j] == '*':
            result *= num_list[j+1]
        elif operator[j] == '/':
            result = int(result/num_list[j+1])

    ans.append(result)

print(max(ans))
print(min(ans))
