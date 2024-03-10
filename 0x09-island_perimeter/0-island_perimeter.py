#!/usr/bin/python3
"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    count = 0
    height = len(grid)
    width = len(grid[0])
    for index, cell in enumerate(grid):
        for ind, sq in enumerate(cell):
            if sq == 1:
                if ind - 1 < 0:
                    count += 1
                else:
                    if cell[ind - 1] == 0:
                        count += 1
                if width <= ind + 1:
                    count += 1
                else:
                    if cell[ind + 1] == 0:
                        count += 1
                if index - 1 < 0:
                    count += 1
                else:
                    if grid[index - 1][ind] == 0:
                        count += 1
                if height <= index + 1:
                    count += 1
                else:
                    if grid[index + 1][ind] == 0:
                        count += 1

    return count