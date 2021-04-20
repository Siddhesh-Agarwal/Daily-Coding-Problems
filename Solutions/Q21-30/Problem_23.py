'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''

def ShortestPath(matrix, start, end):
    positions = [start]
    x1, y1 = start
    x2, y2 = end
    while True:
        if x1 == x2 and y1 == y2:
            return len(positions) - 1

        can_go_Up = all([x1 > 0, not matrix[x1-1][y1], (x1-1, y1) not in positions])
        can_go_Left = all([y1 > 0, not matrix[x1][y1-1], (x1, y1-1) not in positions])
        can_go_Down = all([x1 < len(matrix) - 1, not matrix[x1+1][y1], (x+1, y) not in positions])
        can_go_Right = all([y1 < len(matrix[x1]) - 1, not matrix[x1][y1+1], (x1, y1+1) not in positions])

        if x >= end[0]:
            if y >= end[1]:
                if can_go_Up and (x > end[0] or not can_go_Down) :           #* Check to go UP
                    x -= 1
                    positions.append((x,y))
                elif can_go_Down and (x < end[0] or not can_go_Up):          #* Check to go DOWN
                    x += 1
                    positions.append((x,y))
                elif can_go_Right and (y < end[1] or not can_go_Left):       #* Check to go RIGHT
                    y += 1
                    positions.append((x,y))
                elif can_go_Left and (y > end[1] or not can_go_Right):       #* Check to go LEFT
                    y -= 1
                    positions.append((x,y))

            else:
                    if can_go_Up and (x > end[0] or not can_go_Down) :       #* Check to go TOP
                        x -= 1
                        positions.append((x,y))
                    elif can_go_Down and (x < end[0] or not can_go_Up):      #* Check to go BOTTOM
                        x += 1
                        positions.append((x,y))
                    elif can_go_Right and (y < end[1] or not can_go_Left):   #* Check to go RIGHT
                        y += 1
                        positions.append((x,y))
                    elif can_go_Left and (y > end[1] or not can_go_Right) :  #* Check to go LEFT
                        y -= 1
                        positions.append((x,y))

        else:
            if y >= end[1]:
                if can_go_Up and (x > end[0] or not can_go_Down) :           #* Check to go TOP
                    x -= 1
                    positions.append((x,y))
                elif can_go_Down and (x < end[0] or not can_go_Up):          #* Check to go BOTTOM
                    x += 1
                    positions.append((x,y))
                elif can_go_Right and (y < end[1] or not can_go_Left):       #* Check to go RIGHT
                    y += 1
                    positions.append((x,y))
                elif can_go_Left and (y > end[1] or not can_go_Right) :      #* Check to go LEFT
                    y -= 1
                    positions.append((x,y))

            else:
                if can_go_Up and (x > end[0] or not can_go_Down) :           #* Check to go TOP
                    x -= 1
                    positions.append((x,y))               
                elif can_go_Down and (x < end[0] or not can_go_Up):          #* Check to go BOTTOM
                    x += 1
                    positions.append((x,y))
                elif can_go_Right and (y < end[1] or not can_go_Left):       #* Check to go RIGHT
                    y += 1
                    positions.append((x,y))
                elif can_go_Left and (y > end[1] or not can_go_Right) :      #* Check to go LEFT
                    y -= 1
                    positions.append((x,y))
