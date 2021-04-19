'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

def FindIntersectingNode(a: list, b: list):
    l = min([len(a), len(b)])
    for i in range(l):
        if a[i] == b[i]:
            return a[i]
    return None

if __name__ == '__main__':
    a = list(map(int, input().split(' -> ')))
    b = list(map(int, input().split(' -> ')))    
    print(FindIntersectingNode(a, b))