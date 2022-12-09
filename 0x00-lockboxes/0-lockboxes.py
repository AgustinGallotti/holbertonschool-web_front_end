#!/usr/bin/python3


""" lockboxes - unlock the correct box, Return: True or false """

def canUnlockAll(boxes):
    """ n number """
    key = [0]

    for n in key:
        for correct in boxes[n]:
            if correct not in key and correct < len(boxes):
                key.append(correct)
    if len(key) == len(boxes):
        return True
    return False

    for n in key:
        for correct in boxes[n]:
            if correct not in key and correct < len(boxes):
                key.append(correct)
    if len(key) == len(boxes):
        return True
    return False