"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

from random import randrange


def selectRandom(x):
    res = 0
    count = 0
    count += 1

    if count == 1:
        res = x
    else:
        i = randrange(count)
        if i == count - 1:
            res = x
    return res


stream = [i for i in range(10)]
n = len(stream)

for i in range(n):
    print("Random number from first", (i + 1), "numbers is", selectRandom(stream[i]))
