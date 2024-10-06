import threading

class ThreadSafeStack:
    def __init__(self):
        self.stack = []
        self.lock = threading.Lock()
    
    def push(self, data):
        with self.lock:
            self.stack.append(data)
    
    def pop(self):
        with self.lock:
            if not self.stack:
                raise IndexError("Stack Underflow")
            return self.stack.pop()
    
    def peek(self):
        with self.lock:
            if not self.stack:
                return None
            return self.stack[-1]
    
    def isEmpty(self):
        with self.lock:
            return len(self.stack) == 0
    
    def size(self):
        with self.lock:
            return len(self.stack)
