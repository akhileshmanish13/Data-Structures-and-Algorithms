class Node(object):

    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)


    def insert(self,data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data , node.leftChild)

        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleVoilation(data, node)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a Leaf Node")
                del node
                return None

            if not node.leftChild:
                print("Removing node with single right child")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("Removing node with single left child")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing Node with two children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node       # If there is just a single node

        node.height = max( self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1


    # def settleVoilation(self,data, node):

        balance = self.calcBalance(node)

    #     Case 1 --> Doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0 :
            # print("Left Left heavy situtaion.....")
            return self.rotateRight(node)

    #     Case 2 --> Doubly right heavy situation
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            # print("Right Right heavy situation.....")
            return self.rotateLeft(node)

    #     Case 3 --> Left Right situation
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            # print("Left Right heavy situation.....")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

    #     Case 4 --> Right Left situation
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            # print("Right Left heavy situation.....")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node

    def getPredecessor(self, node):

         if node.rightChild:
             return self.getPredecessor(node.rightChild)

         return node

    def settleVoilation(self,data, node):

        balance = self.calcBalance(node)

    #     Case 1 --> Doubly left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left Left heavy situtaion.....")
            return self.rotateRight(node)

    #     Case 2 --> Doubly right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print("Right Right heavy situation.....")
            return self.rotateLeft(node)

    #     Case 3 --> Left Right situation
        if balance > 1 and data > node.leftChild.data:
            print("Left Right heavy situation.....")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

    #     Case 4 --> Right Left situation
        if balance < -1 and data < node.rightChild.data:
            print("Right Left heavy situation.....")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node

    def calcHeight(self, node):

        if not node:
            return -1

        return node.height

    # If it return value > 1, then it is doubly left heavy situation --> right rotation
    # If it return value <-1, then it is doubly right heavy situation --> left rotation

    def calcBalance(self, node):

        if not node:
            return 0

        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def traverse(self):

        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print("%d" %node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def rotateRight(self, node):

        print("Rotating to the right on node", node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) +1

        return tempLeftChild

    def rotateLeft(self, node):

        print("Rotating to the left on node", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) +1

        return tempRightChild

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)

avl.remove(5)
avl.remove(4)

avl.traverse()