from collections import deque


def solution(begin, target, words):
    answer = 0

    # begin부터 시작해서 글자가 하나만 다른 단어들을 큐에 넣는다.
    # target과 같으면 탐색을 종료

    queue = deque()
    queue.append([begin, 0])
    visited = [False] * (len(words))
    success = False

    while queue:
        test, cnt = queue.popleft()

        if test == target:
            success = True
            answer = cnt
            break

        for i, word in enumerate(words):  # 모든 word를 검사
            if visited[i]:
                continue

            diff_char_cnt = 0
            for j in range(len(word)):  # word 각 글자를 검사 with test
                if test[j] != word[j]:
                    diff_char_cnt += 1
            if diff_char_cnt == 1:
                queue.append([word, cnt+1])
                answer = cnt + 1
                visited[i] = True

    return answer if success else 0
