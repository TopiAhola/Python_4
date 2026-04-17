import time
from functools import cache


@cache
def fast_fib(n):
    if n < 2:
        return 1
    else:
        return fast_fib(n - 1) + fast_fib(n - 2)



def fib_recursive(n, computed = None):

    if computed is None:
        computed = [1, 1] #first 2 fibocacci numbers

    #if number is an index of cache
    if n < len(computed):
        return computed[n]

    #else
    else:
        computed.append(fib_recursive(n - 1, computed) + fib_recursive(n - 2, computed))
        return computed[n]


def fib2(n, computed=None):
    if computed is None:
        computed = [1, 1]  # first 2 fibocacci numbers

    if n < 2:
        return 1

    # if number is an index of cache
    if n < len(computed):
        return computed[n]

    # else
    else:
        computed.append(fib2(n - 1, computed) + fib2(n - 2, computed))
        return computed[n]


def fib_without_cache(n):
    if n < 2:
        return 1
    else:
        return fib_without_cache(n - 1) + fib_without_cache(n - 2)


def fib(n, computed = None):

    if computed is None:
        computed = [1, 1] #first 2 fibocacci numbers

    #if number is an index of cache
    if n < len(computed):
        return computed[n]

    #else
    else:
        #add numbers to computed list
        for index in range(2, n + 1):
            if index <= len(computed):
                computed.append( computed[index - 1] + computed[index - 2] )

        #return
        return computed[n]


def fib_no_list(n):

    #if number is
    if n < 2:
        return 1

    #else
    else:
        fib_number = 0
        n_1 = 1
        n_2 = 1
        for index in range(2, n + 1):
            fib_number = n_1 + n_2
            n_2 = n_1
            n_1 = fib_number

        #return
        return fib_number



#main
if __name__ == '__main__':
    print(fib_recursive(10))

    cumulative_difference = 0
    cumulative_time = 0
    cumulative_runtime1 = 0
    cumulative_runtime2 = 0

    for i in range(100):
        print(f'loop {i}')
        for number in range(1, 1000):
            #faster
            start_time = time.time()
            fib_number1 = fib(number)
            runtime1 = time.time() - start_time

            #slower
            start_time = time.time()
            fib_number2 = fib_no_list(number)
            runtime2 = time.time() - start_time

            difference = runtime2 - runtime1

            cumulative_difference += difference
            cumulative_time = cumulative_time + runtime1 + runtime2
            cumulative_runtime1 += runtime1
            cumulative_runtime2 += runtime2

            assert fib_number1 == fib_number2

            #print(f'Fibonacci number: {number} fast runtime: {runtime1} slow runtime: {runtime2} difference: {difference}')

    print(f'Cumulative difference: {cumulative_difference}')
    print(f'Cumulative time: {cumulative_time}')
    print(f'Cumulative runtime1: {cumulative_runtime1}')
    print(f'Cumulative runtime2: {cumulative_runtime2}')
    print(f'Relative difference: {cumulative_runtime2 / cumulative_runtime1}')
