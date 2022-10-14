import ctypes


class Stack(object):
    """
    Implementation of the stack data structure
    """

    def __init__(self, n):
        self.l = 0
        self.n = n
        self.stack = self._create_stack(self.n)

    def _create_stack(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()

# push(item) - store an element on the stack
# pop() - remove an element from the stack
# top() - get the top data element of the stack, without removing it
# full() - check if stack is full
# empty() - check if the stack is empty
# size() - return the size of the stack
