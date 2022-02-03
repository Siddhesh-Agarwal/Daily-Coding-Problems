"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through ElevationMap. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""


def ShortestPath(matrix, start, end):
    positions = [start]
    x, y = start
    while True:
        if (x, y) == end:
            return len(positions) - 1

        can_go_up = x - 1 >= 0 and not matrix[x - 1][y] and (x - 1, y) not in positions
        can_go_left = (
            y - 1 >= 0 and not matrix[x][y - 1] and (x, y - 1) not in positions
        )
        can_go_down = (
            x + 1 < len(matrix) and not matrix[x + 1][y] and (x + 1, y) not in positions
        )
        can_go_right = (
            y + 1 < len(matrix[x])
            and not matrix[x][y + 1]
            and (x, y + 1) not in positions
        )

        if x >= end[0]:
            if y >= end[1]:
                if can_go_up and (x > end[0] or not can_go_down):  # * Check to go UP
                    x -= 1
                    positions.append((x, y))
                elif can_go_down and (
                    x < end[0] or not can_go_up
                ):  # * Check to go DOWN
                    x += 1
                    positions.append((x, y))
                elif can_go_right and (
                    y < end[1] or not can_go_left
                ):  # * Check to go RIGHT
                    y += 1
                    positions.append((x, y))
                elif can_go_left and (
                    y > end[1] or not can_go_right
                ):  # * Check to go LEFT
                    y -= 1
                    positions.append((x, y))

            else:
                if can_go_up and (x > end[0] or not can_go_down):  # * Check to go TOP
                    x -= 1
                    positions.append((x, y))
                elif can_go_down and (
                    x < end[0] or not can_go_up
                ):  # * Check to go BOTTOM
                    x += 1
                    positions.append((x, y))
                elif can_go_right and (
                    y < end[1] or not can_go_left
                ):  # * Check to go RIGHT
                    y += 1
                    positions.append((x, y))
                elif can_go_left and (
                    y > end[1] or not can_go_right
                ):  # * Check to go LEFT
                    y -= 1
                    positions.append((x, y))

        else:
            if y >= end[1]:
                if can_go_up and (x > end[0] or not can_go_down):  # * Check to go TOP
                    x -= 1
                    positions.append((x, y))
                elif can_go_down and (
                    x < end[0] or not can_go_up
                ):  # * Check to go BOTTOM
                    x += 1
                    positions.append((x, y))
                elif can_go_right and (
                    y < end[1] or not can_go_left
                ):  # * Check to go RIGHT
                    y += 1
                    positions.append((x, y))
                elif can_go_left and (
                    y > end[1] or not can_go_right
                ):  # * Check to go LEFT
                    y -= 1
                    positions.append((x, y))

            else:
                if can_go_up and (x > end[0] or not can_go_down):  # * Check to go TOP
                    x -= 1
                    positions.append((x, y))
                elif can_go_down and (
                    x < end[0] or not can_go_up
                ):  # * Check to go BOTTOM
                    x += 1
                    positions.append((x, y))
                elif can_go_right and (
                    y < end[1] or not can_go_left
                ):  # * Check to go RIGHT
                    y += 1
                    positions.append((x, y))
                elif can_go_left and (
                    y > end[1] or not can_go_right
                ):  # * Check to go LEFT
                    y -= 1
                    positions.append((x, y))
