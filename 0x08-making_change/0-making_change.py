#!/usr/bin/python3
"""
Find the minimum number of coins required from a stack of coins
with varying values to reach a specified total amount.
"""


def makeChange(coins, total):
    """
    Find the minimum number of coins required from a stack of coins
    with varying values to reach a specified total amount.
    """
    sum = 0
    if (total <= 0):
        return 0
    coins.sort(reverse=True)
    for i in coins:
        if (total < i):
            pass
        q, r = divmod(total, i)
        total = r
        sum += q
    if (total != 0):
        return -1
    return sum
