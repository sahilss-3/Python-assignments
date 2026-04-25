class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def safe_pop(self):
        if self.stack == []:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Popped Element:", s.safe_pop())
print("Popped Element:", s.safe_pop())
print("Popped Element:", s.safe_pop())
print("Popped Element:", s.safe_pop())