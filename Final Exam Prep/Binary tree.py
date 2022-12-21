#implement a binary tree

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rightChild = self.rightChild
            self.rightChild = t

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

r = BinaryTree('a')
# print(r.getVal())
# print(r.getLeftChild())
r.insertLeft('b')
# print(r.getLeftChild().getVal())
r.insertRight('c')
# print(r.getRightChild().getVal())
r.getRightChild().setVal('hello')
# print(r.getRightChild().getVal())
r.preorder()
r.inorder()
