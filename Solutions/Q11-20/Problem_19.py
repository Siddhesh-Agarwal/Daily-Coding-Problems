'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''

def MinimizeColorCost(arr: list):
    results = []
    Helper(arr, results, 0, -1, 0, "")
    return min(results)

def Helper(arr: list, results: list, curr_house: int, prev_color: int, curr_cost: int, curr_seq: str):
    if curr_house == len(arr):
        results.append((curr_cost, curr_seq))
        return
    for i in range(0, len(arr[0])):
        if i != prev_color:
            Helper(arr, results, curr_house + 1, i, arr[curr_house][i] + curr_cost, curr_seq + str(i))