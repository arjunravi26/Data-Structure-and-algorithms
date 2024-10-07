class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, data):
        if not self.head:
            self.head = Node(data)
            return True
        new_data = Node(data)
        self.head.prev = new_data
        new_data.next = self.head
        self.head = new_data
        return True

    def insert_end(self, data):
        if not self.head:
            self.head = Node(data)
            return True
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(data)
        new_node.prev = temp
        temp.next = new_node
        return True
    def insert_pos(self):
        pass

    def traverse(self):
        if not self.head:
            return None
        temp = self.head
        while temp:
            print(f"{temp.data}", end="<->" if temp.next else "")
            temp = temp.next


dll = LinkedList()
dll.insert_begin(5)
dll.insert_begin(10)
dll.insert_begin(1)
dll.traverse()
dll.insert_end(80)
dll.insert_end(70)
dll.traverse()
