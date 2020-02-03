"""
@Author: Alex Waweru
"""
import timeit


def dynamic_programming_change_maker(coin_value_list, change, min_coins, coins_used):
   for cents in range(change+1):
      coin_count = cents
      new_coin = 1
      for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
               coin_count = min_coins[cents-j]+1
               new_coin = j
      min_coins[cents] = coin_count
      coins_used[cents] = new_coin
   return min_coins[change]


# compute dynamic time
def dynamic_time():
    SETUP_CODE = "from __main__ import dynamic_programming_change_maker"
    TEST_CODE = "dynamic_programming_change_maker([1,5,10,21,25],63,[0]*64, [0]*64)"

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
    dynamic_time()