#!/usr/bin/python3
"""Function that determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """Function that takes a list of coins and use
       it to calculate the change that the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for n in coin:
            while(total >= n):
                counter += 1
                total -= n
        if total == 0:
            return counter
        return -1
