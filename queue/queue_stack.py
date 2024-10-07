#  Implement queue using two stack

class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s1 and not self.s2:
            return False
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s1 and not self.s2:
            return False
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def isEmpty(self):
        return self.s2 and self.s1
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())