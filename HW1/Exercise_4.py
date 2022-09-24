import time

def sum1(n):
    t0 = time.time()
    total = 0
    for x in range(1,n+1):
        total += x
    return total, time.time() - t0

# Python decorators
# Hint: Google "execution time with decorators in Python"


def sum1(n):
    """
    Sum of numbers between 1 and n
    inputs:
        n (int): last integer to add
    outputs:
        total (int): total sum
    """

    total = 0
    # range goes only until (n+1)-1
    for x in range(1,n+1):
        total += x
    return total
