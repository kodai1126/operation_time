#maxheap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _compare(self, item1, item2):
        return item1 > item2

    def _upheap(self, index):
        while index > 0 and not self._compare(self.heap[self._parent(index)], self.heap[index]):
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def insert(self, value):
        self.heap.append(value)
        self._upheap(len(self.heap) - 1)