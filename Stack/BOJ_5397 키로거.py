# 커서는 스택 2개를 사용해서 관리
# 스택1은 main_stack, 스택2는 커서 뒤에 있는 문자들로, sub_stack
"""
"<" 입력 시 원래 스택1을 pop해서 스택2에 저장. 이후 입력은 스택1에
">" 입력 시 스택2을 pop해서 스택1에 저장
"-" 입력시 스택1을 pop해서 버림
"""
from collections import deque

case = int(input())

for _ in range(case):
    input_list = list(input())
    main_stack = deque()
    sub_stack = deque()

    for x in input_list:
        if x == '<':
            if not main_stack:
                continue
            else:
                sub_stack.append(main_stack.pop())
        elif x == '>':
            if not sub_stack:
                continue
            else:
                main_stack.append(sub_stack.pop())
        elif x == '-':
            if not main_stack:
                continue
            else:
                main_stack.pop()
        else:
            main_stack.append(x)
    # 이 부분을 빠트림. 남은 sub_stack을 main으로 옮겨야됨
    main_stack.extend(reversed(sub_stack))
    print(''.join(main_stack))
