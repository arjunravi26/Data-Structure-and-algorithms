class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data)
        self.count += 1
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            raise IndexError("Queue Underflow")
        dequeued_value = self.head.data
        self.head = self.head.next
        self.count -= 1
        if self.head is None:
            self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def __len__(self) -> int:
        return self.count

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.data
            temp = temp.next


ll_queue = Queue()
print(len(ll_queue))
for i in ll_queue:
    print(i)

ll_queue.enqueue(10)
ll_queue.enqueue(20)
ll_queue.enqueue(30)
for i in ll_queue:
    print(i)

ll_queue.deque()
for i in ll_queue:
    print(i)
