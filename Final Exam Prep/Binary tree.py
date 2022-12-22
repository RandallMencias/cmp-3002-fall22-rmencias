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
        temp = []
        temp.append(self.key)
        if self.leftChild:
            temp.extend(self.leftChild.preorder())
        if self.rightChild:
            temp.extend(self.rightChild.preorder())
        return temp

    def inorder(self):
        temp = []
        if self.leftChild:
            temp.extend(self.leftChild.inorder())
        temp.append(self.key)
        if self.rightChild:
            temp.extend(self.rightChild.inorder())
        return temp

    def postorder(self):
        temp = []
        if self.leftChild:
            temp.extend(self.leftChild.postorder())
        if self.rightChild:
            temp.extend(self.rightChild.postorder())
        temp.append(self.key)
        return temp


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')

print(r.preorder())
print(r.inorder())
print(r.postorder())



