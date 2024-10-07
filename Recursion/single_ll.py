class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, data):
        new_value = Node(data)
        if not self.head:
            self.head = new_value
            return True
        new_value.next = self.head
        self.head = new_value
        return True

    def insert_end(self, data):
        new_value = Node(data)
        if not self.head:
            self.head = new_value
            return True
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_value
        return True

    def insert_pos(self, pos, data):
        new_value = Node(data)
        current_pos = 1
        temp = self.head
        if pos < 0:
            return False
        if pos == 1:
            new_value.next = self.head
            self.head = new_value
            return True

        while temp.next and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1
        if not temp:
            return False
        new_value.next = temp.next
        temp.next = new_value
        return True

    def delete_beg(self):
        if not self.head:
            return False
        if self.head.next:
            self.head = self.head.next
            return True
        else:
            self.head = None

    def delete_end(self):
        if not self.head:
            return False
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return True

    def delete_pos(self, pos):
        if not self.head:
            return None
        temp = self.head
        current_pos = 1

        while temp and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1
        if not temp:
            return False
        if temp.next.next:
            temp.next = temp.next.next
            return True
        temp.next = None

    def search(self, data):
        if not self.head:
            return False
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def get_head(self):
        return self.head

    def traverse(self):
        if not self.head:
            return None
        temp = self.head
        while temp:
            print(f"{temp.data}", end="->"if temp.next else "\n")
            temp = temp.next

    def reverse(self):
        if not self.head:
            return None
        temp = self.head
        prev = None
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev
        return True

    def insert_af_node(self, node, data):
        if not self.head:
            return None
        if node is None:
            return False
        temp = self.head
        while temp:
            if temp == node:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return True
            temp = temp.next

    def insert_bf_node(self, node, data):
        if not self.head:
            return None
        if node is None:
            return False
        temp = self.head
        while temp.next:
            if temp.next == node:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return True
            temp = temp.next


ll = LinkedList()
ll.insert_begin(10)
ll.insert_begin(20)
ll.insert_begin(1)
ll.insert_end(30)
ll.insert_end(50)
ll.traverse()
ll.insert_pos(3, 100)
ll.traverse()

ll.delete_beg()
ll.delete_end()
ll.delete_pos(3)
ll.traverse()
print(ll.search(20))
ll.reverse()
ll.traverse()
head = ll.get_head()
ll.insert_af_node(head.next, 1099)
ll.traverse()
ll.insert_bf_node(head.next, 2000)
ll.traverse()
