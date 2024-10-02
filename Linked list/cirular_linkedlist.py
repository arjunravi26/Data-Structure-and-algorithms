class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node

        else:
            temp = self.head
            new_node.next = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            self.head = new_node

    def insert_end(self, data):
        if not self.head:
            return False
        temp = self.head
        new_node = Node(data)
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_pos(self, pos, data):
        if not self.head:
            return False
        temp = self.head
        new_node = Node(data)
        current_pos = 0
        while temp and current_pos < pos - 1:
            current_pos += 1
            temp = temp.next
        if not temp:
            return False
        next_node = temp.next
        temp.next = new_node
        if next_node:
            new_node.next = next_node

    def delete_begin(self):
        if not self.head:
            return False
        old_head = self.head
        self.head = self.head.next
        temp = self.head
        while temp.next != old_head:
            temp = temp.next
        temp.next = self.head

    def delete_end(self):
        if not self.head:
            return False
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        while temp.next != self.head:
            print(f"{temp.data}", end="<->")
            temp = temp.next
        print(temp.data)

    def reverse(self):
        if not self.head:
            return False
        temp = self.head
        prev = self.head
        while temp.next != self.head:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        temp.next = prev
        self.head.next = temp
        self.head = temp

    def search(self, data):
        if not self.head:
            return False
        temp = self.head
        while temp.next != self.head:
            if temp.data == data:
                return True
            temp = temp.next
        if temp.data == data:
            return True
        return False


cll = CircularLinkedList()
cll.insert_begin(0)
cll.insert_begin(10)
cll.insert_end(30)
cll.insert_end(9)
print(cll.length())
cll.display()
cll.reverse()
cll.display()
print(cll.search(8))
cll.delete_begin()
cll.display()
cll.delete_end()
cll.display()
print(cll.length())
cll.reverse()
cll.display()
print(cll.search(30))
