#!/usr/bin/python3
""" Island Perimeter """
# 0 represents water
# 1 represents land


def island_perimeter(grid):
    """Function that returns the perimeter of the island described in grid."""
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check each side (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
