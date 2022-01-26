Case = int(input())
for _ in range(Case):
    N, target_index = list(map(int, input().split()))
    queueList = list(map(int, input().split()))
    cnt = 0

    while True:
        max_idx = queueList.index(max(queueList))

        if max_idx == 0:
            queueList.pop(0)
            cnt += 1

            if target_index == 0:
                break
            target_index -= 1
        else:
            for _ in range(max_idx):
                queueList.append(queueList.pop(0))  # 앞으로 보내기
                # target index 맞춰주기
                if target_index == 0:
                    target_index = len(queueList) - 1
                else:
                    target_index -= 1
    print(cnt)


"""------------------------
   ------------------------
"""

case = int(input())

for _ in range(case):

    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(priority, idx) for idx, priority in enumerate(queue)]

    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1

            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
