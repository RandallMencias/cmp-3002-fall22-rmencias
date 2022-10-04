from time import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pandas import DataFrame


def clock(func):
    def inner(args):
        start = time() * 10 ** 9
        answer = func(args)
        end = time() * 10 ** 9
        print("Execution Time:" + str(end - start) + "s\nTotal Sum = " + str(answer) + "\n")
        return answer, end - start

    return inner


@clock
def sum1(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


@clock
def sum2(n):
    total = n * (n + 1) // 2
    return total


def main(n):
    print("n = " + str(n) + "\nLoop:")
    sum1(n)
    print("Gaussian addition:")
    sum2(n)


if __name__ == "__main__":
    print("N Test")
    main(5)
    main(8)
    main(103)
    main(527)
    print("N timings")
    runtime1 = [sum1(x)[1] for x in [1, 10, 100, 1000, 10000,100000,1000000,10000000,100000000,1000000000]]
    runtime2 = [sum2(x)[1] for x in [1, 10, 100, 1000, 10000,100000,1000000,10000000,100000000,1000000000]]
    x = [1, 10, 100, 1000, 10000, 100000, 1000000,10000000,100000000,1000000000]
    print(runtime1)
    print(runtime2)
    plt.plot(x, runtime1, label= "Sum1")
    plt.plot(x, runtime2, label="Sum2")
    plt.xlabel('n')
    plt.ylabel('runtime')
    plt.title("Loop Vs Gaussian Sum")
    plt.grid()
    plt.show()



























