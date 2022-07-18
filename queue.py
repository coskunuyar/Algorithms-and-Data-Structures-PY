class QueueNode:
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None
    
    def clear_connections(self):
        self.next = None
        self.prev = None
        return self

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self , value):
        new_node = QueueNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self.length

    def un_shift(self):
        shifted_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return shifted_node.clear_connections()


queue = Queue()
queue.push(0)
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)

print(queue.un_shift().__dict__)
print(queue.un_shift().__dict__)