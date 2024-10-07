from collections import deque


class Stack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if self.isEmpty():
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        value = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return value

    def isEmpty(self):
        return len(self.q1) == 0


stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())
