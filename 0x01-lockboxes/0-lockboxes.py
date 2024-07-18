#!/usr/bin/python3
""" Lock Boxes """

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """
    opened = [0] * len(boxes)
    stack = [0]

    while stack:
        current = stack.pop()
        if opened[current] == 0:
            opened[current] = 1
            for box in boxes[current]:
                if box < len(boxes) and not opened[box]:
                    stack.append(box)

    return all(opened)
