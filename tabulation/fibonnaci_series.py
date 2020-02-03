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


def tabulated_fibonacci(n):
    calculated_values = [0, 1]

    for i in range(2, n+1):
        calculated_values.append(calculated_values[i - 1] + calculated_values[i - 2])

    return calculated_values[n]


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
    SETUP_CODE = "from __main__ import tabulated_fibonacci"
    TEST_CODE = "tabulated_fibonacci(15)"

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