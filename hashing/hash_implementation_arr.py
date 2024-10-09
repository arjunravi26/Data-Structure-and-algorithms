class Hash:
    def __init__(self) -> None:
        self.capacity = 7
        self.count = 0
        self.arr = [None] * self.capacity

    def _hash(self, key):
        return key % self.capacity

    def load_balancer(self):
        load_balancer = self.count / self.capacity
        if load_balancer > 0.8:
            self.capacity *= 2
            self.resize()

    def insert(self, key):
        self.load_balancer()
        idx = self._hash(key)
        if self.arr[idx] is None:
            self.arr[idx] = key
            self.count += 1
        return idx

    def delete(self, key):
        idx = self._hash(key)
        if self.arr[idx]:
            self.count -= 1
            value = self.arr[idx]
            self.arr[idx] = None
            return value
        return False

    def search(self, key):
        idx = self._hash(key)
        if self.arr[idx]:
            return self.arr[idx]
        return False

    def display(self):
        for i in self.arr:
            if i is not None:
                print(i, end=",")
        print()

    def resize(self):
        old_arr = self.arr
        self.arr = [None] * self.capacity
        self.count = 0
        for i in old_arr:
            if i:
                self.insert(i)
        return


hash_table = Hash()
print(hash_table.insert(10))
print(hash_table.insert(20))
print(hash_table.insert(30))
print(hash_table.insert(40))
print(hash_table.delete(30))
print(hash_table.search(20))
print(hash_table.insert(0))
print(hash_table.insert(99))
print(hash_table.insert(91))
print(hash_table.insert(92))
print(hash_table.insert(93))
print(hash_table.insert(90))
print(hash_table.insert(98))
hash_table.display()
print(hash_table.capacity)
