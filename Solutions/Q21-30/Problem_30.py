'''
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two ElevationMap get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

def WaterTrapped(ElevationMap):
    if len(ElevationMap) < 3:
        return 0

    WaterHeld = 0
    left = 0
    right = len(ElevationMap) - 1
    left_max = 0
    right_max = 0
    
    while left <= right:
        if ElevationMap[left] < ElevationMap[right]:
            if ElevationMap[left] > left_max:
                left_max = ElevationMap[left]
            else:
                WaterHeld += left_max - ElevationMap[left]
            left += 1
        else:
            if ElevationMap[right] > right_max:
                right_max = ElevationMap[right]
            else:
                WaterHeld += right_max - ElevationMap[right]
            right -= 1
    return WaterHeld