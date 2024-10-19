#  Implement queue using two stack

class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s1 and not self.s2:
            raise IndexError("Dequeue from empty queue")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def isEmpty(self):
        return not (self.s2 or self.s1)


queue = Queue()
queue.enqueue(10)[10, 20, 30]
queue.enqueue(20)[30, 20, 10]  # queue using stack(first drop)
queue.enqueue(30)[10, 20, 30]
print(queue.dequeue())[10, 20, 30]  # stack using queue(last drop)
print(queue.dequeue())
