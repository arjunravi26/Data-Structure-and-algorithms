class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, data):
        new_value = Node(data)
        if not self.head:
            self.head = new_value
            self.head.prev = new_value
            self.head.next = new_value
            return True
        tail = self.head.prev
        new_value.prev = tail
        new_value.next = self.head
        tail.next = new_value
        self.head.prev = new_value
        self.head = new_value

    def insert_end(self, data):
        new_value = Node(data)
        if not self.head:
            self.head = new_value
            self.head.next = new_value
            self.head.prev = new_value
            return True
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_value
        new_value.prev = temp
        new_value.next = self.head
        self.head.prev = new_value

    def insert_pos(self, pos, data):
        if not self.head or pos < 1:
            return False
        if pos == 1:
            return self.insert_begin(data)

        current_pos = 1
        temp = self.head
        while temp.next != self.head and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1
        new_value = Node(data)
        new_value.next = temp.next
        new_value.prev = temp
        temp.next = new_value
        new_value.next.prev = new_value
        return True

    def traverse(self):
        temp = self.head
        if not temp:
            return None
        while temp.next != self.head:
            print(f"{temp.data}", end="<->")
            temp = temp.next
        print(temp.data)


circular_linkedlist = CircularLinkedList()
circular_linkedlist.insert_begin(10)
circular_linkedlist.insert_begin(2)
circular_linkedlist.insert_end(100)
circular_linkedlist.insert_end(78)
circular_linkedlist.traverse()
circular_linkedlist.insert_pos(1, 1109)
circular_linkedlist.insert_pos(3, 9109)
circular_linkedlist.traverse()
