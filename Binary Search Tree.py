class Node(object):

    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    # Insert Root node in BST

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # Insert Left Child and Right Child in BST

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild )
            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    # Removing node from BST


    def removeNode(self,data, node):
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

        return node

    def getPredecessor(self, node):

         if node.rightChild:
             return self.getPredecessor(node.rightChild)

         return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)


    # Searching Minimum value in BST

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)

        return node.data

    # Searching Maximum value in BST

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)

        return node.data

    # In-order Traversal in BST

    def traverse(self):
        if self.root:
            return self.inOrderTraversal(self.root)

    def inOrderTraversal(self, node):
        if node.leftChild:
            self.inOrderTraversal(node.leftChild)

        print("%s" %node.data)

        if node.rightChild:
            self.inOrderTraversal(node.rightChild)

bst = BinarySearchTree()
bst.insert(32)
bst.insert(10)
bst.insert(55)
bst.insert(79)
# bst.insert(16)
# bst.insert(19)
# bst.insert(1)
# bst.insert(23)
bst.remove(10)

# print(bst.getMinValue())
# print(bst.getMaxValue())
bst.traverse()




