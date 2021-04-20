'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2
'''

import itertools

def rooms_req(arr):
    input_data = [' '.join(str(j) for j in i) for i in arr]
    combinations = set()
    rooms = 0
    
    for c in itertools.combinations(input_data, 2):
        a = set(range(*(int(n) for n in c[0].split())))
        b = set(range(*(int(i) for i in c[1].split())))
        
        if not a.intersection(b) == combinations:
            rooms += 1
            
    if rooms > 0:
        return rooms
    else:
        return 1

if __name__ == "__main__":
    arr = eval(input('Enter list on timings: '))
    print(rooms_req(arr))
