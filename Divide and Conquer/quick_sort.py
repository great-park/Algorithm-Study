import random


# def qsort(data):
#     if len(data) <= 1:
#         return data

#     left, right = list(), list()
#     pivot = data[0]

#     for i in range(1, len(data)):
#         if data[i] < pivot:
#             left.append(data[i])
#         else:
#             right.append(data[i])

#     return qsort(left) + [pivot] + qsort(right)


def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    # list comprehension으로 더욱 간결하게
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)


data = random.sample(range(100), 10)

print(qsort(data))
