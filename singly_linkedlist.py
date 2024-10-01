class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_pos(self, data, pos):
        if pos < 1:
            print("Position must be 1 or greater.")
            return False
        node = Node(data)
        if pos == 1:
            node.next = self.head
            self.head = node
            return True
        current = self.head
        current_pos = 1
        while current and current_pos < pos - 1:
            current = current.next
            current_pos += 1
        if not current:
            print("No such position exist")
            return False
        node.next = current.next
        current.next = node
        return True

    def delete_data(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return True
            current_node = current_node.next

    def delete_first(self):
        if not self.head:
            return False
        self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return False
        current_node = self.head
        if not current_node.next:
            self.head = None
            return True
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        return True

    def search(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            return True
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def find_length(self):
        length = 0
        if not self.head:
            return length
        current_node = self.head
        while current_node.next:
            length += 1
        return length+1

    def detect_cycle(self):
        if not self.head:
            return False
        first = self.head
        current_node = self.head
        while current_node.next != None or current_node.next != first:
            current_node = current_node.next
        if current_node.next == first:
            return True
        else:
            return False

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} -> ")
            current = current.next
