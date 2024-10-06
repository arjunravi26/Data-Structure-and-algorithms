# Array implementation of static stack
class Stack:
    def __init__(self, max_size) -> None:
        self.pointer = -1
        self.size = max_size
        self.stack = [None] * max_size

    def push(self, data):
        if self.isFull():
            raise OverflowError("Stack Overflow")
        self.pointer += 1
        self.stack[self.pointer] = data
        return f"Successfully inserted {data}"

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack Underflow")
        popped_value = self.stack[self.pointer]
        self.stack[self.pointer] = None
        self.pointer -= 1
        return popped_value

    def isEmpty(self):
        return self.pointer == -1

    def isFull(self):
        return self.pointer == self.size - 1

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.pointer]

    def __str__(self) -> str:
        return f"{self.stack[:self.pointer+1]}"


if __name__ == "__main__":
    stack = Stack(max_size=5)
    stack.push(10)
    stack.push(10)
    stack.push(10)
    stack.push(10)
    stack.push(10)
    print(stack)
    stack.push(3)
    stack.push(0)
    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
