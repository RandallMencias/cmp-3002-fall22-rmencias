import ctypes


class Array(object):
    """
    Implementation of the array data structure
    """

    def __init__(self, n):
        """
        Initialize the class
        """
        self.l = 0
        self.n = n
        self.array = self._create_array(self.n)

    def _create_array(self, n):
        """
        Creates a new array of capacity n
        """
        return (n * ctypes.py_object)()



class Array(Array):

    def __init__(self, n, values=None):
        """
        Initialize empty array
        """
        self.l = 0
        self.n = n
        self.array = self._create_array(self.n)
        if values:
            self.initialize_array(values)

    def initialize_array(self, values):
        """
        Initialize array
        """
        if self.n != len(values):
            raise ValueError("element count different than capacity")
        for item in values:
            self.array[self.l] = item
            self.l += 1

    def list_array(self):
        """
        List elements of the array
        using list comprehension
        """
        return ", ".join(str(x) if x is not None else '_' for x in self)

    def list_array2(self):
        y = []
        for x in self:
            if x is not None:
                y.append(str(x))
            else:
                y.append('_')
        return ", ".join(y)

    def __getitem__(self, item_index):
        """
        Return element at item_index
        """
        if (item_index < 0) or (item_index >= self.n):
            raise IndexError('index out of range!')
        try:
            x = self.array[item_index]
        except ValueError:
            x = None
        return x

    def __setitem__(self, item_index, item):
        """
        Set element at item_index
        """
        if (item_index < 0) or (item_index >= self.n):
            raise IndexError('index out of range!')
        self.array[item_index] = item

    def insert_to_tail(self, item):
        """
        Add new item to the tail of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.array[self.l] = item
        self.l += 1

    def insert_to_head(self, item):
        """
        Add new item to the beginning of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        i = self.l
        while (i > 0):
            self.array[i] = self.array[i - 1]
            i -= 1
        self.array[0] = item
        self.l += 1

    def insert(self, index, element):
        """
        implementation of insert
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        if (index < 0) or (index > self.l):
            raise IndexError('index out of range!')
        x = self.l
        while x > index:
            self.array[x] = self.array[x - 1]
            x -= 1
        self.array[index] = element
        self.l += 1

    def delete_tail(self):
        """
        Deletes var at tail of array
        """
        if self.l == 0:
            raise ValueError("no items to delete")
        self.array[self.l-1] = None
        self.l -= 1

    def delete_head(self):
        """
        Deletes var at head of array
        """
        if self.l == 0:
            raise ValueError("no items to delete")
        self.array[0] = None
        for i in range(0,self.l-1):
            self.array[i] = self.array[i+1]
        self.l -= 1
        self.array[self.l]= None

    def delete(self, index):
        """
        Deletes var at index
        """
        if (index < 0) or (index >= self.l):
            raise IndexError('index out of range!')

        self.array[index] = None
        for i in range(index, self.l-1):
            self.array[i] = self.array[i+1]

        self.l -= 1
        self.array[self.l] = None



def main():
    x = Array(5,[3,2,1,4,5])
    print(x.list_array2())
    x.delete_head()
    print(x.list_array2())
    x.insert_to_head(133)
    print(x.list_array2())
    x.delete_tail()
    print(x.list_array2())
    x.delete(2)
    print(x.list_array2())

if __name__ == "__main__":
    main()
