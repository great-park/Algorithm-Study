def selectionSort(data):
    for i in range(len(data)-1):
        lowest = i
        for j in range(i+1, len(data)):
            if data[lowest] > data[j]:
                lowest = j
        data[lowest], data[i] = data[i], data[lowest]
    return data


data = [3, 1, 2, 4, 6, 5]
print(selectionSort(data))
