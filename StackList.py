class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.item == []
    
    def push(self, item):
        self.item.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
from pythonds.basic.stack import Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

class Stack:
    def __init__(self):
        selt.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.item[0]
    
    def size(self):
        return len(self.items)
    
s = Stack()
s.push('hello')
s.push('true')
print(s.pop())


        