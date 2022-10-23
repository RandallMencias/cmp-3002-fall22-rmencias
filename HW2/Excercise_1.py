class Node:
    """
    Implementation of a node
    """

    def __init__(self, val=None):
        self.val = val
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node


class Singly_linked_list(object):

    def __init__(self, head_node=None):
        self.head_node = head_node

    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

    def insert_head(self, new_node):
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_tail(self, new_node):
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)

    def insert_middle(self, new_node, value):
        # insert in the middle
        # A -> B -> C -> null
        # A -> B -> R -> C -> null
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)

    def delete(self):
        node = self.head_node
        self.head_node = node.next_node
        node = None


class Stack(object):
    def __init__(self):
        self.stack = self._create_stack()

    def _create_stack(self):
        """
        Creates a new stack of capacity n
        """
        return Singly_linked_list()

    def push(self, item):
        """
            Add new item to the stack
            """

        self.stack.insert_head(Node(item))

    def pop(self):
        """
            Remove an element from the stack
        """
        self.stack.delete()

    def top(self):
        """
            Show the top element of the stack
            """
        return self.stack.head_node

    # def full(self):
    #     """
    #         Is the stack full?
    #         """
    #     return self.l == self.n
        # if self.l == self.n:
        #    return True
        # return False

    def empty(self):
        """
            Is the stack empty?
            """
        return self.stack.head_node is not None

    # def size(self):
    #     """
    #         Return size of the stack
    #         """
    #     return self.l

    def print(self):
        self.stack.list_traversed()



S = Stack()
S.push(1)
S.push(2)
S.push(4)
S.push(-1)
S.print()

