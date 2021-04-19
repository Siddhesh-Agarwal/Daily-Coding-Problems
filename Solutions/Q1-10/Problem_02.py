'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def product(arr: list):
    product = 1
    for i in arr:
        product *= i
    return product

def main(arr):
    lst = [[arr[j] for j in range(len(arr)) if j != i] for i in range(len(arr))]
    return list(map(product, lst))

if __name__ == '__main__':
    arr = list(input())
    print(main(arr))
