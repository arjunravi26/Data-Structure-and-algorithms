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
            print("Queue is full")
            return False
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size
        print(self.rear)
        self.count += 1
        return data
    # delete from front

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return False
        deleted_value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        print(self.front)
        self.count -= 1
        return deleted_value

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def peek(self):
        if self.isEmpty():
            return False
        return self.queue[self.front]

    def __len__(self):
        return self.count

    def __iter__(self):
        if self.count == 0:
            return False
        count = self.count - 1
        for i in self.queue:
            yield i

    def __str__(self) -> str:
        return f"{self.queue}"


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
