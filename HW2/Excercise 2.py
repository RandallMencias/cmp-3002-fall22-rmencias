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

    class Stack(Stack):
        def push(self, item):
            """
            Add new item to the stack
            """
            if self.l == self.n:
                raise ValueError("no more capacity")
            self.stack[self.l] = item
            self.l += 1

        def pop(self):
            """
            Remove an element from the stack
            """
            # self.l = 0
            # 0 is equivalent to False
            # any number != 0 is True
            if not self.l:
                raise ('stack is empty')
            c = self.stack[self.l - 1]
            self.stack[self.l] = ctypes.py_object
            self.l -= 1
            return c

        def top(self):
            """
            Show the top element of the stack
            """
            return self.stack[self.l - 1]

        def full(self):
            """
            Is the stack full?
            """
            return self.l == self.n
            # if self.l == self.n:
            #    return True
            # return False

        def empty(self):
            """
            Is the stack empty?
            """
            return self.l == 0
            # if self.l == 0:
            #    return True
            # return False

        def size(self):
            """
            Return size of the stack
            """
            return self.l

        def reverse(self):
            prev = self.top
            cur = self.top
            cur = cur.next
            succ = None
            prev.next = None

            while (cur != None):
                succ = cur.next
                cur.next = prev
                prev = cur
                cur = succ

            self.top = pre




