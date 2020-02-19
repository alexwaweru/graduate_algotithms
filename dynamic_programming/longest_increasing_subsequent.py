"""
@Author: Alex Waweru
"""
import timeit


def longest_increasing_subsequent(sequence):
    # default longest subsequence length is 1
    longest_subsequence_len = [1] * len(sequence)

    # loop through all values in the subsequence
    for i in range(0, len(sequence), 1):
        max_len = longest_subsequence_len[i]
        # for each value loop through all the previous values
        for j in range(i,-1,-1):
            temp = longest_subsequence_len[j]
            # find the value that:
            # 1. is less than the current value
            # 2. has the subsequence with the longest length
            if  temp + 1 >= max_len and sequence[i] > sequence[j]:
                max_len = temp + 1
        longest_subsequence_len[i] = max_len
    print(longest_subsequence_len)

# compute dynamic time
def dynamic_time():
    SETUP_CODE = "from __main__ import longest_increasing_subsequent"
    TEST_CODE = "longest_increasing_subsequent([5,7,4,-3,9,1,10,4,5,8,9,3])"

    # timeit.repeat statement
    times = timeit.repeat(
        setup = SETUP_CODE,
        stmt=TEST_CODE,
        repeat=1,
        number=1
    )

    # printing minimum exec. time
    print('dynamic programming time complexity: {}'.format(min(times)))


if __name__ == "__main__":
    dynamic_time()