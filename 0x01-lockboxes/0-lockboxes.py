#!/usr/bin/python3
""" module for the functions canUnlockAll"""


def canUnlockAll(boxes):
    """Check if it's possible to unlock all boxes in a given list of boxes"""
    opened_boxes = [0]
    for box in opened_boxes:
        for key in boxes[box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.append(key)
    return len(opened_boxes) == len(boxes)
