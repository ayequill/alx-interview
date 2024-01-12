#!/usr/bin/python3
""" Module for lockboxes """


def canUnlockAll(boxes):
    """ Function for lockboxes """
    opened_boxes = {0}

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == len(boxes)
