'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

from time import sleep

f = input("Enter function: ")

n = int(input("Enter time in milliseconds: "))
sleep(n / 100)

print(eval(f + '()'))