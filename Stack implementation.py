class Stack:
    def __init__(self):
        self.Stack = []

    def isEmpty(self):
        return self.Stack ==[]

    # push operation

    def push(self,data):
        self.Stack.append(data)

    # Pop operation

    def pop(self):
        data = self.Stack[-1]
        del self.Stack[-1]
        return data

    # Peek operation

    def peek(self):
        # print(self.Stack[-1])
        return self.Stack[-1]

    def size1(self):
        return len(self.Stack)

stack = Stack()
stack.push(4)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size1())
print("Popped:", stack.pop())
print("popped:", stack.pop())
print(stack.size1())
print("peek:",stack.peek())
stack.push(45)
stack.push(48)

print(stack.size1())