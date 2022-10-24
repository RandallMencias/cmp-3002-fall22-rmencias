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
        vip = None
        priority = 0
        contador = 0
        for x in range(self.l):
            if self.queue[x][1] > priority:
                priority = self.queue[x][1]
                vip = self.queue[x]

        if self.queue[self.l - 1] != vip:
            for x in range(self.l):
                if self.queue[x] == vip:
                    self.queue[contador] = self.queue[x + 1]
                    contador -= 1
                else:
                    self.queue[contador] = self.queue[x]
                contador += 1

        self.queue[self.l - 1] = None
        self.l -= 1
        return vip[0]





        # for x in range(self.l):
        #     if self.queue[x] is not vip:
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
