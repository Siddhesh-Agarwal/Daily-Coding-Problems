'''
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''
def is_parent_locked(node):
    if not node.parent:
        return False
    elif node.parent.locked:
        return True
    else:
        return is_parent_locked(node.parent)

def update_parent(node, enable_locks):
    increment = 1 if enable_locks else -1
    if node.parent:
        node.parent.locked_descendants += increment
        update_parent(node.parent, enable_locks)

class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.LEFT = None
        self.RIGHT = None
        self.locked = None
        self.locked_branches = None
    
    def __str__(self):
        return f"val={self.val};locked={self.locked};locked_descendants={self.locked_descendants}"

    def is_locked(self):
        '''returns whether the node is locked'''
        return self.locked

    def lock(self):
        '''Attempts to lock the node.
        If it cannot be locked, then it returns False.
        Otherwise, it locks the node and returns True.'''
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = True
            update_parent(node=self, enable_locks=True)
            return True

    def unlock(self):
        '''Attempts to unlock the node. 
        If it cannot be unlocked, then it returns False.
        Otherwise, it unlocks the node and returns True.'''
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = False
            update_parent(node=self, enable_locks=False)
            return True
