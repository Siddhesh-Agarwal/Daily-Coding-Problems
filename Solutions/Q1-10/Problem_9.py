'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def find_max_sum(arr):
    incl = 0
    excl = 0
     
    for i in arr:
        temp = excl if excl > incl else incl
        incl = excl + i
        excl = temp
    return excl if excl > incl else incl

if __name__ == "__main__":
    array = int(input("Enter an array: "))
    print(find_max_sum(array))