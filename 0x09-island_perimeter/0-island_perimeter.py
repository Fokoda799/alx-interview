#!/usr/bin/python3
""" Island Perimeter """
# 0 represents water
# 1 represents land


def island_perimeter(grid):
    """ Function that returns the perimeter of the island described in grid """
    if not grid:
        return None
    if not isinstance(grid, list):
        return None
    if not isinstance(grid[0], list):
        return None
    if not isinstance(grid[0][0], int):
        return None
    if len(grid) < 1 or len(grid) > 100:
        return None
    if len(grid[0]) < 1 or len(grid[0]) > 100:
        return None
    if 1 in grid[0] or 1 in grid[-1]:
        return None

    perimeter = 0

    for i in range(1, len(grid) - 1):
        if grid[i][0] == 1 or grid[i][-1] == 1:
            return None
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
