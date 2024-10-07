class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def insert_beg(self, data):
        new_node = Node(data)
        self.count += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        self.count += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_beg(self):
        if not self.head:
            raise IndexError("Underflow")
        else:
            self.count -= 1
            self.head.next.prev = None
            self.head = self.head.next

    def delete_end(self):
        if not self.tail:
            raise OverflowError("Queue overflow")
        else:
            self.count -= 1
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def isEmpty(self):
        return self.head == None

    def peek_first(self):
        if self.head:
            return self.head.data

    def peek_end(self):
        if self.tail:
            return self.tail.data

    def traverse(self):
        if not self.head:
            return None
        temp = self.head
        while temp:
            print(f"{temp.data}", end="<->" if temp.next else "\n")
            temp = temp.next

    def __len__(self):
        return self.count


dq = DoublyQueue()
print(dq.isEmpty())
dq.insert_beg(10)
dq.insert_beg(5)
dq.insert_beg(1)
dq.insert_end(20)
dq.insert_end(50)
dq.traverse()
dq.delete_beg()
dq.delete_end()
dq.traverse()
print(dq.peek_end())
print(dq.peek_first())
print(len(dq))
