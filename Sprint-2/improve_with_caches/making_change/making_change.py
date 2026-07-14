from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1])

cache={}
def ways_to_make_change_helper(total: int, coins: List[int], coin_index: int=0) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    key = (total, coin_index)
    if total == 0:
        return 1
    if total < 0 or coin_index == len(coins):
        return 0  
    if key in cache:
        return cache[key]
    
    ways = 0
    coin = coins[coin_index]
    count= 0
    while coin * count <= total:
        total_from_coins = coin * count
        ways += ways_to_make_change_helper(total - total_from_coins, coins, coin_index=coin_index+1)
        count += 1
    cache[key] = ways
    return ways


