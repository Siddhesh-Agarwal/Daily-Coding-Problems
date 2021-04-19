'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def CheckSumOfPair(arr, k):
    for i in range(len(arr)):
        x = arr[i]
        if k-x in arr[i+1:]:
            return True
        if x > k//2:
            break
    else:
        return False

if __name__ == '__main__':
	arr = list(input())
	k = int(input())
	print(CheckSumOfPair(arr, k))
