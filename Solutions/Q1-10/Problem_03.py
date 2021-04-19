'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node(' + repr(self.val) + ', ' + repr(self.left) + ', ' + repr(self.right) + ')'

    def __eq__(self, other):
        if isinstance(other, Node):
            return all([self.val == other.val, self.left == other.left, self.right == other.right])
        return False

    def __hash__(self):
        return hash((self.val, self.left, self.right))

serialise = repr
deserialise = eval

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialise(serialise(node)).left.left.val == 'left.left'
