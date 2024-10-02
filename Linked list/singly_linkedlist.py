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

    def print_list(self):
        """Print the contents of the list in a readable format."""
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()
