#!/usr/bin/python3
""" Lock Boxes """

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """
    visited = [False] * len(boxes)
    stack = [0]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for box in boxes[current]:
                if not visited[box]:
                    stack.append(box)

    return all(visited)
