class node :
    def __init__(self, data):
        self.data = data
        self.next = None

class myqueue :
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    #membuat method enqueue, dequeue, peek, printQueue
    def enqueue(self, data):
        newNode = node(data)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    def printQueue(self):
        if self.isEmpty():
            print("Queue kosong")
        else:
            current = self.head
            while current != None:
                print(current.data, end=" ")
                current = current.next
            print()
#test
q = myqueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printQueue()
print("dequeue:", q.dequeue())
q.printQueue()
print("peek:", q.peek())