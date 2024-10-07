class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        """Insert a new node at the beginning of the list."""
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        """Insert a new node at the end of the list."""
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_pos(self, data, pos):
        """Insert a new node at a specified position."""
        if pos < 1:
            print("Error: Position must be 1 or greater.")
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
            print("Error: No such position exists.")
            return False
        node.next = current.next
        current.next = node
        return True

    def delete_data(self, data):
        """Delete the first node that contains the specified data."""
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
        return False

    def delete_first(self):
        """Delete the first node in the list."""
        if not self.head:
            print("Error: The list is empty.")
            return False
        self.head = self.head.next
        return True

    def delete_last(self):
        """Delete the last node in the list."""
        if not self.head:
            print("Error: The list is empty.")
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
        """Search for a node containing the specified data."""
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def find_length(self):
        """Return the length of the list."""
        length = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            length += 1
        return length

    def detect_cycle(self):
        """Detect if there is a cycle in the list using Floyd's algorithm."""
        if not self.head:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def reverse(self):
        if not self.head:
            return None
        if self.head.next is None:
            return self.head
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def sort_list(self):
        if not self.head:
            return self.head
        temp = self.head
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data
                    swapped = True
                temp = temp.next

    def find_middle(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def delete_middle(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return True

    def detect_cycle(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        else:
            return False

    def split(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        first_half = self.head
        second_half = slow
        prev.next = None
        return first_half, second_half

    def print_list(self):
        """Print the contents of the list in a readable format."""
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()


singly_linked_list = LinkedList()
singly_linked_list.insert_begin(10)
singly_linked_list.insert_begin(2)
singly_linked_list.insert_begin(28)
singly_linked_list.insert_begin(29)
singly_linked_list.insert_end(100)
singly_linked_list.insert_end(78)
singly_linked_list.print_list()
singly_linked_list.insert_pos(1, 1109)
singly_linked_list.insert_pos(3, 9109)
singly_linked_list.print_list()
singly_linked_list.delete_first()
singly_linked_list.print_list()
print(singly_linked_list.find_length())
print(singly_linked_list.search(2))
print(singly_linked_list.delete_data(9109))
singly_linked_list.print_list()
# singly_linked_list.update_value(78, 80)
singly_linked_list.print_list()
singly_linked_list.reverse()
singly_linked_list.print_list()
singly_linked_list.sort_list()
singly_linked_list.print_list()
singly_linked_list.insert_begin(109)
singly_linked_list.insert_begin(109)
singly_linked_list.print_list()
print(singly_linked_list.find_middle())
singly_linked_list.delete_middle()
singly_linked_list.print_list()
print(singly_linked_list.detect_cycle())
singly_linked_list.print_list()
l1, l2 = singly_linked_list.split()
print(l1.data)
print(l2.data)
