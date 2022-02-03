"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def SmallestPositiveInteger(arr):
    arr = sorted(set(arr))

    for i in arr:
        if i <= 0:
            arr.remove(i)
        else:
            break

    for index, i in enumerate(arr, start=1):
        if index != i:
            return index
    return index + 1


if __name__ == "__main__":
    arr = list(input("Enter a list: "))
    print(SmallestPositiveInteger(arr))
