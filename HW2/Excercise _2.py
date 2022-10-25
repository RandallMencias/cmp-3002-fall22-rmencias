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
        """
        Output: prints list
                """
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

    def reverse(self):
        """
         Reverses list
                """
        node = self.head_node
        prev = None # Creates variable for previuos node
        while node is not None: # original head needs to end on None
            next = node.next_node #creates a next variable
            node.next_node = prev # prev node.next_node is asign as next node
            prev = node #inverst position between node and next node
            node = next #moves on to the next set of nodes
        self.head_node = prev # head becomes last prev node


