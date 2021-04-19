'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

from pickle import dump, load

class Answer:
    def record(order_id):
        with open("logs.dat", "ab+") as f:
            dump(order_id, f)

    def get_last(i):
        with open("logs.dat", "rb") as f:
            logs = list(load(f))
            return logs[-i]