# Hash implementation using division method
class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None


class DefaultHash:
    def __init__(self) -> None:
        self.size = 7
        self.arr = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def lookup(self, key):
        idx = self._hash(key)
        return self.arr[idx]

    def insert(self, key):
        idx = self._hash(key)
        new_node = Node(key)
        if self.arr[idx] is None:
            self.arr[idx] = new_node
            return

        current = self.arr[idx]
        while current:
            if current.val == key:
                return
            if current.next is None:
                current.next = new_node
            current = current.next

    def delete(self, key):
        idx = self._hash(key)
        if not self.arr[idx]:
            return None
        current = self.arr[idx]
        while current.next:
            if current.next.val == key:
                current.next = current.next.next
            current = current.next

    def seeAll(self):
        for i in self.arr:
            current = i
            while current:
                print(current.val, end="->" if current.next else "\n")
                current = current.next


dh = DefaultHash()
dh.insert(9)
dh.insert(10)
dh.insert(11)
dh.insert(12)
dh.insert(13)
dh.insert(15)
dh.insert(13)
dh.insert(16)
dh.insert(19)
dh.insert(20)
dh.insert(80)
dh.delete(20)
# print(dh.lookup(10))
# dh.delete(10)
# print(dh.lookup(10))
# print(hash("addfdfsd"))
print(dh.seeAll())

