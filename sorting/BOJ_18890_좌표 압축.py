from sys import stdin
input = stdin.readline
N = int(input())
data = list(map(int, input().split()))
# set으로 감싸서 중복 제거 후 정렬
sorted_data = sorted(set(data))

# 해쉬 테이블 사용 key = 실제 값,  value = 인덱스(맨 앞은 0, 즉 자신보다 작은 수가 0개)
dic = {sorted_data[i]: i for i in range(len(sorted_data))}

for x in data:  # 원래 순서에서 값을 꺼낸 뒤
    print(dic[x], end=' ')
