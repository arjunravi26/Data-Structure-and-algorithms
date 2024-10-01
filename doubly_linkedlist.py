class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_pos(self, data, pos):
        if pos < 1:
            print("No such position")
            return

        new_node = Node(data)
        if pos == 1:
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return

        temp = self.head
        current_pos = 1

        while temp and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1

        if not temp:
            print("Position out of range")
            return False

        new_node.next = temp.next

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node
        new_node.prev = temp

    def delete(self, data):
        if not self.head:
            return False

        temp = self.head

        if temp.data == data:
            if temp.next:
                temp.next.prev = None
            self.head = temp.next
            return True

        while temp and temp.next:
            if temp.next.data == data:
                node_to_delete = temp.next
                temp.next = node_to_delete.next

                if temp.next:
                    temp.next.prev = temp

                return True
            temp = temp.next

        return False

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data} <-> ", end="")
            temp = temp.next
        print("None")
