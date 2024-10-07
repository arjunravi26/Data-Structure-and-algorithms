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

    def delete_begin(self):
        if self.head is None:
            return False
        temp = self.head
        if temp.next:
            temp.next.prev = None
            self.head = temp.next
        else:
            self.head = None
        return True

    def delete_end(self):
        if self.head is None:
            return False
        temp = self.head
        if temp.next is None:
            self.head = None
            return True
        while temp.next.next:
            temp = temp.next
        temp.next.prev = None
        temp.next = None
        return True

    def search(self, data):
        if self.head is None:
            return False
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data}", end="<->" if temp.next else "\n")
            temp = temp.next
        print()

    def display_reverse(self):
        if not self.head:
            return False
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(f"{temp.data}", end="<->" if temp.prev else "\n")
            temp = temp.prev
        return True

    def get_len(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse(self):
        temp = self.head
        if not temp:
            return None
        prev = None
        while temp:
            next_node = temp.next  # None
            temp.next = prev  # prev 4
            temp.prev = next_node  # None
            prev = temp
            temp = next_node
        self.head = prev
        return True

    def update_value(self, old_value, new_value):
        temp = self.head
        if not temp:
            return False
        while temp:
            if temp.data == old_value:
                temp.data = new_value
            temp = temp.next
        return False

    def clear(self):
        self.head = None
    def split(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        first_half = self.head
        slow.prev = None
        second_half = slow
        prev.next = None
        return first_half,second_half


# Create an instance of DoublyLinkedList
dll = DoublyLinkedList()

# Insert values at the beginning
dll.insert_begin(10)
dll.insert_begin(20)

# Insert values at the end
dll.insert_end(30)
dll.insert_end(40)

# Insert value at a specific position
dll.insert_pos(25, 3)  # Insert 25 at position 3

# Display the list
dll.display()

# Display the list in reverse
dll.display_reverse()

print(dll.get_len())
dll.reverse()
dll.display()
dll.update_value(252, 100)
dll.display()
dll.clear()
dll.display()
