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
        temp = self.head.prev
        temp.next = new_value
        new_value.prev = temp
        new_value.next = self.head
        self.head.prev = new_value

    def insert_pos(self, pos, data):
        if not self.head or pos < 1 or pos > self.length() + 1:
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

    def delete_begin(self):
        if not self.head:
            return False
        if self.head.next != self.head:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next
        else:
            self.head = None
        return True

    def delete_end(self):
        if not self.head:
            return False
        if self.head.prev != self.head:
            temp = self.head.prev
            self.head.prev = temp.prev
            temp.prev.next = self.head
        else:
            self.head = None
        return True

    def delete_data(self, data):
        if not self.head:
            return False
        temp = self.head
        if temp.data == data:
            return self.delete_begin()
        while temp.next != self.head:
            if temp.data == data:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return True
            temp = temp.next
        if temp.data == data:
            temp.prev.next = self.head
            self.head.prev = temp.prev
            return True
        else:
            return False

    def length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            count += 1
        return count

    def reverse(self):
        if not self.head:
            return False
        temp = self.head
        while temp.next != self.head:
            next_val = temp.next
            temp.next,temp.prev = temp.prev,temp.next
            temp = next_val
        temp.next,temp.prev = temp.prev,self.head
        self.head = temp

    def update_value(self, data, new_data):
        if not self.head:
            return False
        temp = self.head
        while temp.next != self.head:
            if temp.data == data:
                temp.data = new_data
                return True
            temp = temp.next
        if temp.data == data:
            temp.data = new_data
            return True
        else:
            return False

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
        else:
            return False

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
circular_linkedlist.delete_begin()
circular_linkedlist.traverse()
print(circular_linkedlist.length())
print(circular_linkedlist.search(2))
print(circular_linkedlist.delete_data(9109))
circular_linkedlist.traverse()
circular_linkedlist.update_value(78, 80)
circular_linkedlist.traverse()
circular_linkedlist.reverse()
circular_linkedlist.traverse()
