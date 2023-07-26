def bubblesort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True

        if swap == False:
            break
    return data


data1 = [10, 1, 6, 7, 9]

print(bubblesort(data1))
