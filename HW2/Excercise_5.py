import random
from time import time


def clock(func):
    def inner(*args, **kwargs):
        start = time() * 10 ** 9
        answer = func(*args, **kwargs)
        end = time() * 10 ** 9
        # print("Execution Time:" + str(end - start) + "ns\nTotal Sum = " + str(answer) + "\n")
        return answer, end - start

    return inner


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
        a = ''
        while node:
            a = a + str(node.val) + "->"
            node = node.next_node
        print(a)

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


@clock
def transform(int1, int2, int3):
    list1 = Singly_linked_list()
    list2 = Singly_linked_list()
    list3 = Singly_linked_list()
    list4 = Singly_linked_list()

    n = len(str(int1))
    sum = int1 + int2 + int3
    a = 0
    for i in range(n - 1, -1, -1):
        list1.insert_head(Node(int(str(int1)[i])))
        list2.insert_head(Node(int(str(int2)[i])))
        list3.insert_head(Node(int(str(int3)[i])))
    for i in range(len(str(sum)) - 1, -1, -1):
        list4.insert_head(Node(int(str(sum)[i])))

    # list1.list_traversed()
    # list2.list_traversed()
    # list3.list_traversed()
    # print("_"*10*n+"__")
    list4.list_traversed()


def ran(i):
    return (random.randint(i, i * 10))


runtime1 = [transform(ran(10 ** i), ran(10 ** i), ran(10 ** i))[1] for i in range(51)]

print(runtime1)
