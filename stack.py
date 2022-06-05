'''
Created on Jun 5, 2022

@author: Jim Yin
'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
out_of_stack = my_stack.pop()
print(out_of_stack)
