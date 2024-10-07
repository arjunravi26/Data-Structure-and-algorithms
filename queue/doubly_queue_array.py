class Deque:
    def __init__(self, size):
        """Initialize the deque with a given size."""
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        """Check if the deque is full."""
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)

    def is_empty(self):
        """Check if the deque is empty."""
        return self.front == -1

    def insert_front(self, item):
        if self.is_full():
            print("Deque is full. Cannot insert at the front.")
            return
        if self.is_empty():
            self.rear = self.front = 0
        else:
            if self.front == 0:
                self.front = self.size - 1
            else:
                self.front -= 1
        self.deque[self.front] = item

    def insert_rear(self, item):
        if self.is_full():
            print("Deque is full")
            return
        if self.is_empty():
            self.rear = self.front = 0
        else:
            if self.rear == self.size - 1:
                self.rear = 0
            else:
                self.rear += 1
        self.deque[self.rear] = item

    def delete_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        deleted_value = self.deque[self.front]
        self.deque[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return deleted_value

    def delete_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        deleted_value = self.deque[self.rear]
        self.deque[self.rear] = None
        if self.rear == self.front:
            self.front = -1
            self.rear = -1
        else:
            self.rear -= 1
        return deleted_value

    def peek_front(self):
        if self.is_empty():
            return None
        return self.deque[self.front]

    def peek_rear(self):
        if self.is_empty():
            return None
        return self.deque[self.rear]