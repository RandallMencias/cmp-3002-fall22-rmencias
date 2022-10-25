import ctypes


class PriorityQueue(object):
    """
    Implementation of the queue data structure
    """

    def __init__(self, n):
        self.l = 0
        self.n = n
        self.queue = self._create_queue(self.n)

    def _create_queue(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()

    def enqueue(self, item):
        """
        Add new item to the queue
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.queue[self.l] = item
        self.l += 1

    def deque(self):
        """
        Returns value with highest priority and removes it
        Output: Value of highest priority
                        """
        miv = None
        priority = 0
        contador = 0
        for x in range(self.l): #checks through all the queue
            if self.queue[x][1] > priority: #if priority of one value is bigger than another
                priority = self.queue[x][1] #assigns the priority of Miv
                miv = self.queue[x] #saves Miv

        if self.queue[self.l - 1] != miv: #checks miv isnt the last value
            for x in range(self.l):
                if self.queue[x] == miv:
                    #Skips the Miv Value decreses counter by one to match new size
                    self.queue[contador] = self.queue[x + 1]
                    contador -= 1
                else:
                    #assingns the value of the list by contador to the list of x
                    self.queue[contador] = self.queue[x]
                contador += 1

        self.queue[self.l - 1] = None #deletes last reapeated value
        self.l -= 1
        return miv[0]




        #Alternate method for elminating Miv from queue
        # for x in range(self.l):
        #     if self.queue[x] is not miv:
        #         temp.enqueue(self.queue[x])
        # self.queue = temp.queue
        # self.l -= 1


q = PriorityQueue(10)
q.enqueue((1, 200))
q.enqueue((2, 4))
q.enqueue((0, 1))
q.enqueue((9, 43))
q.enqueue((1, 21))
q.enqueue((3, 12))
q.enqueue((5, 6))
print(q.deque())
print(q.queue[0:q.l])
