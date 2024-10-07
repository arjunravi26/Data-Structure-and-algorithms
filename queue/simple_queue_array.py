from typing import Optional


class Queue:
    def __init__(self, size) -> None:
        self.queue = [None] * size
        self.rear = 0
        self.front = 0
        self.count = 0
        self.size = size
    # insert at rear

    def enqueue(self, data):
        if self.isFull():
            raise OverflowError("Queue is full")
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size
        self.count += 1
    # delete from front

    def dequeue(self) -> Optional[int]:
        if self.isEmpty():
            raise IndexError("deque from an empty queue")
        deleted_value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return deleted_value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

    def peek(self) -> Optional[int]:
        if self.isEmpty():
            return None
        return self.queue[self.front]

    def __len__(self) -> int:
        return self.count

    def __iter__(self):
        if self.isEmpty():
            return iter([])
        idx = self.front
        for _ in range(self.count):
            yield self.queue[idx]
            idx = (idx + 1) % self.size


queue = Queue(5)
for i in queue:
    print(i)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(8)
queue.dequeue()
queue.enqueue(0)
for i in queue:
    print(i)
print(queue)
