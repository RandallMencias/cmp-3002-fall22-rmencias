import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import time


def clock(func):
    def inner(*arg):
        start = time.time()*10 ** 6
        answer = func(*arg)
        end = time.time() * 10 ** 6
        #print("Execution Time:" + str(end - start))
        return answer, (end - start)

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
    def get_tail(self):
        """
        Gets tail
        Output: tail
        """
        node = self.head_node
        while node:
            prev = node
            node = node.next_node
        return prev
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
        Input: Node, value before Node
                        """
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)
    def reverse(self):
        """
        Reverses list
        """
        node = self.head_node
        prev = None
        while node is not None:
            next = node.next_node
            node.next_node = prev
            prev = node
            node = next
        self.head_node = prev


    def delete(self):
        """
        Deletes Head and remplaces with next node
        """
        node = self.head_node
        self.head_node = node.next_node
        node = None


@clock
def transform(int1, int2, int3):
    """
    Transforms 3 Integers to SLl and prints out the sum
    Input: int1, int2, int3
    """
    #Creates lists
    list1 = Singly_linked_list()
    list2 = Singly_linked_list()
    list3 = Singly_linked_list()
    list4 = Singly_linked_list()

    n = len(str(int1))

    #uses string in a reverse lopp to extract the values and insert them to the lists
    for i in range(n-1, -1, -1):
        list1.insert_head(Node(int(str(int1)[i])))
        list2.insert_head(Node(int(str(int2)[i])))
        list3.insert_head(Node(int(str(int3)[i])))

    #reverses the lists
    list1.reverse()
    list2.reverse()
    list3.reverse()
    #creates variable to retain the values of each part of the number
    node1 = list1.head_node
    node2 = list2.head_node
    node3 = list3.head_node
    remainder = 0 #remainder is gonna represent the extra from the sum

    while node1 != None: #cycles through the whole int
        val = (node1.val + node2.val + node3.val + remainder) #adds the values of the respective node as each node is a section of the number, remainder adds the remainder from the last sum
        new_node = Node(val %10) # only keeps the value in its decimal place
        remainder = val // 10 #registers the remainder
        list4.insert_head(new_node) #adds the number to its correct places
        #cycles through the nodes
        node1 = node1.next_node
        node2 = node2.next_node
        node3 = node3.next_node
    if remainder > 0: #adds any last remainder
        list4.insert_head(Node(remainder))

    #restores the lists to normal
    list1.reverse()
    list2.reverse()
    list3.reverse()
    # list4.list_traversed()
    return list4
    #prints the lists
    # list1.list_traversed()
    # list2.list_traversed()
    # list3.list_traversed()
    # print("_"*n*4)
    #



# transform(9999,9999,9999)
#

# print(transform(123559,115439, 115359)[1])

def ran(i):
    return random.randint(10 ** (i - 1), (10 ** i)-1)
#
# for i in range(1,101):
#     print(ran(i))

runtime = [transform(ran(i), ran(i), ran(i))[1] for i in range(1,1001)]
# print(runtime)
plt.plot(runtime)
plt.grid()
plt.xlabel('Character len')
plt.ylabel('runtime')
plt.title("Linked list Sum")
plt.show()
