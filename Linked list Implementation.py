from _ast import If


class node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # Insertion at the starting of the list has O(1) time complexity

    def insertstart(self, data):
        self.size = self.size + 1
        newNode = node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    #  Remove data from the list

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1

        currentNode = self.head
        # previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        # If previousNode is None:
        #     self.head = currentNode.nextNode
        # else:
        #     previousNode.nextNode = currentNode.nextNode

    def size1(self):
        return self.size

    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    #   Insertion at the end of the list has O(n) time complexity

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    #     Traversing of data in the List

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode

linkedList = LinkedList()
linkedList.insertstart(12)
linkedList.insertstart(75)
linkedList.insertstart(98)
linkedList.insertstart(122)
linkedList.insertstart(79)

linkedList.traverseList()
print(linkedList.size1())

linkedList.remove(79)
linkedList.remove(75)
linkedList.remove(98)
linkedList.remove(122)
linkedList.remove(12)

print(linkedList.size1())