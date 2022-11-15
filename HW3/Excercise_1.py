class Node:  # Implements Nodes with code shown in class
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

    # Using what was shown in class the object is implemented
    def list_traversed(self):
        """
        Output: prints list
         """
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

    def insert_head(self, new_node):
        """
        Inserts new head
        Input: Node
        """
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_tail(self, new_node):
        """
                Inserts new tail
                Input: Node
                """
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)

    def insert_middle(self, new_node, value):
        """
                Inserts Node after value
                Input: Node
                value: Node before new Node
                """
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)

    def delete(self):
        """
        Deletes Head and replaces with next node
        """
        node = self.head_node
        self.head_node = node.next_node
        node = None

    # merges 2 lists through recursion


def merge(L1, L2):

    temp = None

    if L1 is None:
        return L2

    if L2 is None:
        return L1

    print(L1.val, L2.val)
    if L1.val <= L2.val:

        temp = L1
        temp.next_node = merge(L1.next_node, L2)
    else:
        print("hola")
        temp = L2
        temp.next_node = merge(L1, L2.next_node)

    return temp


def main():
    list1 = Singly_linked_list()
    list1.insert_head(Node(7))
    list1.insert_head(Node(5))
    list1.insert_head(Node(3))
    list1.insert_head(Node(1))


    list2 = Singly_linked_list()
    list2.insert_head(Node(6))
    list2.insert_head(Node(4))
    list2.insert_head(Node(2))

    list3 = Singly_linked_list()

    list3.head_node = merge(list1.head_node, list2.head_node)
    print("Merge:")
    list3.list_traversed()

if __name__ == '__main__':
    main()
