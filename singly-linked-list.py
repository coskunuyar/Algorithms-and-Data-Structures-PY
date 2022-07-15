class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def clear_connections(self):
        self.next = None
        return self


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self.length

    def un_shift(self, value):
        if self.length == 0:
            return self.push(value)
        else:
            new_node = ListNode(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return ++self.length

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.tail
            self.head = None
            self.tail = None
            return popped_node
        else:
            popped_node = self.tail
            new_tail = self.head
            while new_tail.next:
                if new_tail.next == self.tail:
                    break
                else:
                    new_tail = new_tail.next
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
            popped_node.clear_connections()
            return popped_node

    def shift(self):
        if self.length == 1:
            return self.pop()
        else:
            shifted_node = self.head
            self.head = shifted_node.next
            self.length -= 1
            return shifted_node.clear_connections()

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            current = self.head
            count = 0
            while count != index:
                current = current.next
                count += 1
            return current

    def set(self, index, value):
        found_node = self.get(index)
        if found_node:
            found_node.value = value
            return found_node
        else:
            return None

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.un_shift(value)
        elif index == self.length:
            return self.push(value)
        else:
            new_node = ListNode(value)
            prev_element = self.get(index - 1)
            next_element = self.get(index)
            prev_element.next = new_node
            new_node.next = next_element
            self.length += 1
            return self.length

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return
        else:
            prev_element = self.head
            current_element = self.head.next
            next_element = self.head.next.next

            while next_element and next_element != self.tail:
                current_element.next = prev_element

                prev_element = current_element
                current_element = next_element
                next_element = next_element.next

            if next_element:
                next_element.next = current_element

            current_element.next = prev_element

            temp = self.head
            self.head = self.tail
            self.tail = temp
            self.tail.next = None

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


sample_list = SinglyLinkedList()
sample_list.push(11)
sample_list.push(22)
sample_list.push(33)
sample_list.un_shift(0)

sample_list.insert(2, 999)

sample_list.reverse()
sample_list.traverse()
