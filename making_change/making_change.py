#!/usr/bin/python
import sys


def making_change(amount, denominations, cache=None):
    """Iterative version."""
    print(amount)
    cache = {0: 1} if cache is None else cache
    for coin in denominations:
        for x in range(coin, amount + 1):
            if x in cache:
                cache[x] += cache[x - coin]
            else:
                cache[x] = cache[x - coin]
    return cache[amount]


def making_change(amount, denominations, cache=None):
    """Recursive version. Half as fast."""
    cache = {0: 1} if cache is None else cache
    if amount in cache:
        return cache[amount]
    for coin in denominations:
        for x in range(coin, amount + 1):
            if x in cache:
                cache[x] += making_change(x - coin, denominations, cache)
            else:
                cache[x] = making_change(x - coin, denominations, cache)
    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations),
                                                                     amount=amount))
    else:
        print("Usage: making_change.py [amount]")
