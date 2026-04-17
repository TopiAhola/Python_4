import time


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# main
if __name__ == '__main__':
    print(fib(10))

    for number in range(1, 80):
        start_time = time.time()
        fib_number = fib(number)
        runtime = time.time() - start_time
        print(f'Fibonacci number: {number} runtime: {runtime}')