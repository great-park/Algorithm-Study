import random


def binary_search(data, search):
    print(data)
    if len(data) == 1 and search == data[0]:
        print("찾았다: ", data[0])
        return True
    if len(data) == 1 and search != data[0]:
        print("case a")
        return False
    if len(data) == 0:
        print("case b")
        return False

    medium = len(data)//2

    if search == data[medium]:
        print("찾았다: ", data[medium])
        return True
    else:
        if search > data[medium]:
            binary_search(data[medium:], search)
        else:
            binary_search(data[:medium], search)


data = random.sample(range(14), 10)
data.sort()  # 원본 data 자체를 정렬해서 수정해주는 메소드 주의!
print(data)
binary_search(data, 7)
