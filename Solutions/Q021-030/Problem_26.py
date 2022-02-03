"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass in one pass.
"""


def RemoveFromEnd(iterable, index=1):
    n = len(iterable)
    for position, i in enumerate(iterable):
        if position == n - index:
            iterable.remove(i)
    return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter linked list: ").split(" -> ")))
    index = int(input("Enter index: "))
    print(RemoveFromEnd(arr, index))
