class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def prepend(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def append(self, value):
        temp = Node(value)
        current = self.head

        if not self.head:
            self.head = temp
            temp.next = None

        while current:
            if current.next is None:
                current.next = temp
                temp.next = None
            current = current.next

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        return count

    def search(self, value):
        temp = self.head

        while temp:
            if temp.data == value:
                return True
            temp = temp.next

        return False

    def remove(self, value):
        temp = self.head
        prev = None
        found = False

        while not found:
            if temp.data == value:
                found = True
            else:
                prev = temp
                temp = temp.next

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next


l1 = LinkedList()
l1.prepend(1)
l1.prepend(2)
l1.prepend(3)
l1.printLL()
print()
l1.append(5)
print()
l1.remove(2)
l1.printLL()



