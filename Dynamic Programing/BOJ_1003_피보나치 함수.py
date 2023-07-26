from sys import stdin
input = stdin.readline
T = int(input())

zero_cnt = [1, 0, 1]
one_cnt = [0, 1, 1]

# dp(num-1) + dp(num-2) : num-1에서의 0과 1 호출 횟수 + num-2에서의 0과 1 호출 횟수


def dp(num):
    if num >= len(zero_cnt):
        for i in range(len(zero_cnt), num + 1):
            zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
            one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
    print('{} {}'.format(zero_cnt[num], one_cnt[num]))


for _ in range(T):
    dp(int(input()))
