from sys import stdin
input = stdin.readline

# greedy : 마이너스 구간은 괄호
set = list(input().rstrip().split('-'))

result = 0
# result에 마이너스 구간 빼기
for id, subset in enumerate(set):
    numbers = subset.split('+')
    # 첫 구간은 더하기, 이 후는 빼기
    if id == 0:
        for number in numbers:
            result += int(number)
    else:
        for number in numbers:
            result -= int(number)
print(result)
