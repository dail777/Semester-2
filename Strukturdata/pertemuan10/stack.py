#implementasi dari linked list

#1 kelas node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#2 kelas stack  
class Stack:
    def __init__(self):
        self.top = None
    #method untuk mengecek apakah stack kosong
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False 

    #push
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    #pop
    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
    #method peek / top
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    #display cetak stack
    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

#instance
mystack = Stack()
print(mystack.is_empty()) #True
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.display()
mystack.peek() #30
mystack.pop() #30
print(mystack.is_empty())


