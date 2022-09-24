import time

def clock(func):
    def inner(args):
        start = time.time()
        answer = func(args)
        end = time.time()
        print("Execution Time:" + str(end-start) + "ms\nTotal Sum = " + str(answer))
        return answer
    return inner


@clock
def sum1(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


@clock
def sum2(n):
        total = n * (n + 1) // 2
        return total


def main(n):
    print("n = " +str(n)+"\nLoop:")
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
    for i in range(0,10):
        main(1*(pow(10,i)))
