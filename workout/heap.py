# max heap
class Heap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._hepify_up(len(self.heap) - 1)

    def _hepify_up(self, index):
        idx = index
        parent_idx = (idx-1) // 2
        if idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._hepify_up(parent_idx)

    def delete(self):
        if not self.heap:
            return False
        if len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0] = self.heap.pop()
        self._hepify_down(0)

    def _heapify_down(self, idx):
        largest = idx
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        if left_child < len(self.heap) and largest < self.heap[left_child]:
            largest = left_child
        if right_child < len(self.heap) and largest < self.heap[right_child]:
            largest = right_child
        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self._heapify_down(largest)

    def peek(self):
        return self.heap[0]
