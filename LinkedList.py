class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.size += 1
            return
        else:
            temp = self.head
            while temp:
                if temp.next is None:
                    temp.next = node
                    self.size += 1
                    break
                temp = temp.next

    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.size += 1
            return
        else:
            temp = self.head
            self.head = node
            node.next = temp
            self.size += 1

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.printLL()


