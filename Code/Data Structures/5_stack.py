# Stacks - 02/01/2025

# defining stack class

class Stack:
    # initialize the stack with an empty list
    def __init__(self):
        self.items = []

    # method to push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # pop an item off the stack
    def pop(self):
        # check if the stack is empty before popping
        if not self.is_empty():
            return self.items.pop()
        else:
            return "stack is empty"

    # peek at the top item of the stack without removing it
    def peek(self):
        # check if the stack is empty before peeking
        if not self.is_empty():
            return self.items[-1]
        else:
            return "stack is empty"

    # check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # get the size of the stack
    def size(self):
        return len(self.items)

# creating a stack instance
stack = Stack()

# example usage
stack.push(1)  # push 1 onto the stack
stack.push(2)  # push 2 onto the stack
stack.push(3)  # push 3 onto the stack
print(stack.pop())  # pop and print the top item (3)
print(stack.peek())  # peek and print the top item (2)
print(stack.is_empty())  # check if the stack is empty (false)
print(stack.size())  # print the size of the stack (2)
