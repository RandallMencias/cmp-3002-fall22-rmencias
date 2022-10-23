class Node:
    """
    Implementation of a node
    """

    def __init__(self, val=None):
        self.val = val
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node


class Singly_linked_list:
    """
    Implementation of a singly linked list
    """

    def __init__(self, head_node=None):
        self.head_node = head_node

    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

    def reverse(self):
        node = self.head_node
        prev = None
        while node is not None:
            next = node.next_node
            node.next_node = prev
            prev = node
            node = next
        self.head_node = prev


