from stack_array import Stack


class BrowserHistory:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = None
    
    def visit(self, url):
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = url
        self.forward_stack = Stack()
    
    def back(self):
        if self.back_stack.isEmpty():
            print("No pages in back history.")
            return
        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()
    
    def forward(self):
        if self.forward_stack.isEmpty():
            print("No pages in forward history.")
            return
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()
    
    def current(self):
        return self.current_page

# Example usage
history = BrowserHistory()
history.visit("Page1")
history.visit("Page2")
history.visit("Page3")
print(history.current())
history.back()
print(history.current())
history.forward()
print(history.current())
