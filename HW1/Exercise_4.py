import time

def clock(func):
    def inner(*args, **kwargs):
        start = time.time()
        answer = func(*args, **kwargs)
        print("Execution Time:" + str(time.time()-start) + "ms\n Total Sum = " + str(answer))
        return answer
    return inner



@clock
def sum2(n):
        total = n * (n + 1) // 2
        return total



sum2(5)





