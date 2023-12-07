#!/usr/bin/python3
""" You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened.
    @boxes is a list of lists
    """
    keys = [0]
    # Iterate over the keys and update the list of keys.
    for n in keys:
        for key in boxes[n]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    # Check if the number of keys obtained is equal to the total number of boxes.
    return len(keys) == len(boxes)
