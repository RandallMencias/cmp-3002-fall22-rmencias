import time
import matplotlib.pyplot as plt
def clock(func):
    def inner(*arg, **kwargs):
        start = time.time() * 10 ** 3
        answer = func(*arg, **kwargs)
        time.sleep(0.0000000000000000000000001)
        end = time.time() * 10 ** 3
        # print("Execution Time:" + str(end - start))
        return answer, (end - start)

    return inner

@clock
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)[0]





@clock
def factorial_memoization(n):
    cache = {}

    def recursive_factorial(n):
        # time.sleep(0.0000000001)
        if n in cache.keys():
            return cache[n]
        if n == 1:
            return 1
        else:
            cache[n] = n * factorial(n - 1)[0]
            return cache[n]

    return recursive_factorial(n)


def main():
    # time.sleep(0.0000000001)
    factorial_time = [factorial(i)[1] for i in range(1, 400)]
    factorial_memoization_time = [factorial_memoization(i)[1] for i in range(1,400)]
    plt.plot(factorial_time, label="factorial")
    plt.plot(factorial_memoization_time, label="factorial_memoization")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
