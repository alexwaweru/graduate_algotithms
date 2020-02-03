"""
@Author: Alex Waweru
"""

import timeit


def recursive_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def memorized_fibonacci(n):

    def calculate_fibonacci(computed_fibonacci_values, value):
        if value > len(computed_fibonacci_values)-1:
            computed_fibonacci_values.append(calculate_fibonacci(computed_fibonacci_values, value-1) +\
                                               calculate_fibonacci(computed_fibonacci_values, value-2)
                                             )
            return computed_fibonacci_values[value]
        return computed_fibonacci_values[value]

    values = [0, 1]
    return calculate_fibonacci(values, n)


# compute recursive time
def recursive_time():
    SETUP_CODE = "from __main__ import recursive_fibonacci"
    TEST_CODE = "recursive_fibonacci(15)"

    # timeit.repeat statement
    times = timeit.repeat(
        setup = SETUP_CODE,
        stmt=TEST_CODE,
        repeat=3,
        number=10000
    )

    # printing minimum exec. time
    print('recursive time complexity: {}'.format(min(times)))


# compute dynamic time
def dynamic_time():
    SETUP_CODE = "from __main__ import memorized_fibonacci"
    TEST_CODE = "memorized_fibonacci(15)"

    # timeit.repeat statement
    times = timeit.repeat(
        setup = SETUP_CODE,
        stmt=TEST_CODE,
        repeat=3,
        number=10000
    )

    # printing minimum exec. time
    print('dynamic time complexity: {}'.format(min(times)))


if __name__ == "__main__":
    recursive_time()
    dynamic_time()