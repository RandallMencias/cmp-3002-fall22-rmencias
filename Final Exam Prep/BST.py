#implement a binary search tree

class BinarySearchTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insert(self, node):
        if node < self.key:
            if self.leftChild == None:
                self.leftChild = BinarySearchTree(node)
            else:
                self.leftChild.insert(node)
        else:
            if self.rightChild == None:
                self.rightChild = BinarySearchTree(node)
            else:
                self.rightChild.insert(node)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setVal(self, obj):
        self.key = obj

    def getVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def search(self, node):
        if node == self.key:
            return True
        elif node < self.key:
            if self.leftChild:
                return self.leftChild.search(node)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.search(node)
            else:
                return False

#driver code
r = BinarySearchTree(8)
r.insert(3)
r.insert(10)
r.insert(1)
r.insert(6)
r.insert(14)
r.insert(4)
r.insert(7)
r.insert(13)
r.preorder()
