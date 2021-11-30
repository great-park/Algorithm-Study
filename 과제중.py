class minHeap(object):
    def __init__(self, items):
        self.queue = [None] + items

        for i in range(len(self.queue) // 2, 0, -1):
            self.min_heapify(i)

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return index * 2

    def right_child(self, index):
        return index * 2 + 1

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def insert(self, n):
        self.queue.append(n)
        for i in range(len(self.queue) // 2, 0, -1):
            self.min_heapify(i)

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index == 0:
            return - 1  # empty

        self.swap(1, last_index)
        min_value = self.queue.pop()
        self.min_heapify(1)  # root에서부터 재정렬
        return min_value

    # 임시 root 부터 자식 노드와 값을 비교하며 재정렬하는 함수
    def min_heapify(self, i):
        last_index = len(self.queue) - 1
        left_index = self.left_child(i)
        right_index = self.right_child(i)
        temp_min_index = i  # 일단 자기 자신을 min로 둠 (임시 root노드)

        # 리프 노드에 한해, 임시 루트 노드보다 값이 더 크면, 해당 노드의 인덱스를 루트 인덱스로 변경
        if left_index <= last_index and self.queue[temp_min_index] > self.queue[left_index]:
            temp_min_index = left_index
        if right_index <= last_index and self.queue[temp_min_index] > self.queue[right_index]:
            temp_min_index = right_index

        # 만약 자신이 가장 큰게 아니면 heapify
        if temp_min_index != i:
            self.swap(i, temp_min_index)  # temp_min_index가 루트 노드로 변경
            self.min_heapify(temp_min_index)  # 재정렬 재귀

    def print_heap(self):
        print(self.queue)


min_heap = minHeap([10, 8])
min_heap.insert(4)
min_heap.insert(3)
min_heap.insert(6)
min_heap.insert(11)
min_heap.insert(63)
min_heap.insert(232)
min_heap.insert(75)
min_heap.insert(44)
min_heap.print_heap()
min_heap.delete()
min_heap.print_heap()
min_heap.delete()
min_heap.print_heap()
min_heap.delete()
min_heap.print_heap()
min_heap.delete()
min_heap.print_heap()
min_heap.delete()
min_heap.print_heap()
min_heap.delete()
min_heap.print_heap()