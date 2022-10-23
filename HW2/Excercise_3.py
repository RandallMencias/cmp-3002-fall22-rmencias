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
            raise 'stack is empty'
        c = self.stack[self.l - 1]
        # self.stack[self.l] = ctypes.py_object
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

    def print(self):
        for i in range(self.l):
            print(self.stack[i])


class Queue(object):
    def __init__(self, n):
        self.n = n
        self.stack = self._create_queue(self.n)

    def _create_queue(self, n):
        return Stack(n)

    def enqueue(self, item):
        self.stack.push(item)

    def deque(self):
        temp = Stack(self.stack.l)
        for i in range(self.stack.l-1):
            temp.push(self.stack.top())
            self.stack.pop()
        self.stack.pop()
        for i in range(temp.l):
            self.stack.push(temp.top())
            temp.pop()



    def first(self):
        return self.stack.stack[0]

    def full(self):
        return self.stack.l == self.stack.n

    def empty(self):
        return self.stack.l == 0

    def size(self):
        return self.stack.l

    def print(self):
        for i in range(0, self.stack.l):
            print(self.stack.stack[i])


S = Queue(4)
S.enqueue(1)
S.enqueue(2)
S.enqueue(4)
S.enqueue(-1)
S.print()
S.deque()
print("hopa")
S.print()
print(S.stack.l)


