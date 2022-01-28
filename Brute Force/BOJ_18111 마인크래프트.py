# (0,0) 시작  (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7)
import sys
input = list(sys.stdin.readline().split(' '))
N, M, block_num = int(input[0]), int(input[1]), int(input[2])
ground = [0 for _ in range(N)]
time = 0

for i in range(N):
    ground[i] = list(map(int, sys.stdin.readline().split(' ')))


def dig():  # 최상층인 층부터 1층만 제거하는 함수
    # max에 해당되는 인덱스 구해서 1씩 빼주기
    global time, block_num
    for i in range(N):
        max_value = max(ground[i])
        max_id = [id for id, value in enumerate(
            ground[i]) if value == max_value]
        for id in max_id:
            ground[id] -= 1
            time += 2
            block_num += 1


def fill_up():
    return


def complete():
    temp_list = list()
    for i in range(3):
        # set 타입으로 변경해서 길이가 1 이상이면 다른 값이 들어있음!
        temp = set(ground[i])
        if len(temp) != 1:
            return False
        temp_list.append(temp.pop())
    temp_list = set(temp_list)
    if len(temp_list) != 1:
        return False
    return True


def make():
    while not complete():
        if block_num == 0:
            dig()
        else:
            # 채우냐 파냐 어떻게 판단??
