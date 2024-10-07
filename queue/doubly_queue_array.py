class DoublyQueue:
    def __init__(self,size) -> None:
        self.count = 0
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = []
    def insert_begin(self):
        self.queue[self.rear] = 0
        self.rear = (self.rear + 1) % self.size
    def insert_end(self):
        pass
    def delete_begin(self):
        pass
    def delete_end(self):
        pass
    def peek_first(self):
        pass
    def peek_end(self):
        pass
