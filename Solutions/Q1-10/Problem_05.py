'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def return_first(a, b):
        return a
    return pair(return_first)

def cdr(pair):
    def return_last(a, b):
        return b
    return pair(return_last)

if __name__=='__main__':
    a, b = map(int, input("Plese enter a and b by spacing them (eg: 3 4): ").split())
    pair = cons(a, b)
    print(car(pair))
    print(cdr(pair))
