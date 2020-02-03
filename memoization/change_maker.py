"""
@Author: Alex Waweru
"""
import timeit


def recursive_change_maker(coin_value_list,change):
   min_coins = change
   if change in coin_value_list:
     return 1
   else:
      for i in [c for c in coin_value_list if c <= change]:
         num_coins = 1 + recursive_change_maker(coin_value_list,change-i)
         if num_coins < min_coins:
            min_coins = num_coins
   return min_coins


def dynamic_change_maker(coin_value_list, change, known_results):
   min_coins = change
   if change in coin_value_list:
      known_results[change] = 1
      return 1
   elif known_results[change] > 0:
      return known_results[change]
   else:
       for i in [c for c in coin_value_list if c <= change]:
         num_coins = 1 + dynamic_change_maker(coin_value_list, change-i,
                              known_results)
         if num_coins < min_coins:
            min_coins = num_coins
            known_results[change] = min_coins
   return min_coins


# compute recursive time
def recursive_time():
    SETUP_CODE = "from __main__ import recursive_change_maker"
    TEST_CODE = "recursive_change_maker([1,5,10,21,25],63)"

    # timeit.repeat statement
    times = timeit.repeat(
        setup = SETUP_CODE,
        stmt=TEST_CODE,
        repeat=3,
        number=1
    )

    # printing minimum exec. time
    print('recursive time complexity: {}'.format(min(times)))


# compute dynamic time
def dynamic_time():
    SETUP_CODE = "from __main__ import dynamic_change_maker"
    TEST_CODE = "dynamic_change_maker([1,5,10,21,25],63,[0]*64)"

    # timeit.repeat statement
    times = timeit.repeat(
        setup = SETUP_CODE,
        stmt=TEST_CODE,
        repeat=3,
        number=1
    )

    # printing minimum exec. time
    print('dynamic time complexity: {}'.format(min(times)))


if __name__ == "__main__":
    recursive_time()
    dynamic_time()