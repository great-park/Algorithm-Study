import sys
input = sys.stdin.readline

test_case = int(input())


def recur():
    global N, answer
    N = int(input())
    answer = []
    select_operator(2, '1')
    print()


def select_operator(now, ans):
    global answer
    if now == N+1:
        set_ans(ans)
        return
    # 아스키코드 순으로 호출
    select_operator(now+1, ans+' '+str(now))
    select_operator(now+1, ans+'+'+str(now))
    select_operator(now+1, ans+'-'+str(now))


def set_ans(ans):
    cal_ans = ans.replace(' ', '')
    if eval(cal_ans) == 0:
        print(ans)


for _ in range(test_case):
    recur()
