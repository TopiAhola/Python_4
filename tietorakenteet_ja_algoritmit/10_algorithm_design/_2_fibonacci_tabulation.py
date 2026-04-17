import time




def fib(n, computed = None):

    if computed is None:
        computed = [1, 1] #first 2 fibocacci numbers

    #if number is an index of cache
    if n < len(computed):
        return computed[n]

    #else
    else:
        computed.append(fib(n - 1, computed) + fib(n - 2, computed) )
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




#main
if __name__ == '__main__':
    print(fib(10))

    cumulative_difference = 0
    cumulative_time = 0
    cumulative_runtime1 = 0
    cumulative_runtime2 = 0

    for i in range(100):
        print(f'loop {i}')
        for number in range(1, 1000):
            start_time = time.time()
            fib_number1 =fib(number)
            runtime1 = time.time() - start_time

            start_time = time.time()
            fib_number2 = fib2(number)
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
