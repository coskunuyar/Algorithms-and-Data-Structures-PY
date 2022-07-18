from hashlib import new
import math
from os import curdir


class DoubleListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def clear_connections(self):
        self.next = None
        self.prev = None
        return self


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self ,value):
        new_node = DoubleListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return self.length

    def un_shift(self , value):
        if self.length == 0:
            return self.push(value)
        else:
            new_node = DoubleListNode(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return self.length

    def pop(self):
        popped_node = None
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.tail
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return popped_node.clear_connections()

    def shift(self):
        shifted_node = None
        if self.length == 0:
            return self.pop()
        elif self.length == 1:
            shifted_node = self.head
            self.head = None
            self.tail = None
        else:
            shifted_node = self.head
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return shifted_node.clear_connections()

    def get(self , index):
        if index < 0 or index > self.length-1:
            return
        else:
            mid = math.floor(self.length / 2)
            current = None
            count = None

            if index >= mid:
                current = self.tail
                count = self.length-1
                while count != index:
                    current = current.prev
                    count -= 1
            else:
                current = self.head
                count = 0
                while count != index:
                    current = current.next
                    count += 1
        return current

    def set(self, index , value):
        found_node = self.get(index)
        if found_node:
            found_node.value = value
        else:
            return None

    def insert(self , index , value):
        if index < 0 or index > self.length-1:
            return
        else:
            new_node = DoubleListNode(value)
            prev = self.get(index-1)
            next_node = self.get(index)
            prev.next = new_node
            new_node.prev = prev
            next_node.prev = new_node
            new_node.next = next_node
            self.length += 1
            return self.length

    def remove(self , index):
        if index == 0:
            return self.shift()
        elif index == self.length-1:
            return self.pop()
        else:
            prev = self.get(index-1)
            current = self.get(index)
            next_node = self.get(index + 1)
            prev.next = next_node
            next_node.prev = prev
            self.length -= 1
            return current.clear_connections()


    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

        

list = DoublyLinkedList()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.un_shift(0)

list.insert(3 , 9999)
list.remove(3)
print(list.get(3).__dict__)

# list.traverse()