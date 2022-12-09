#!/usr/bin/python3


""" lockboxes - unlock the correct box, Return: True or false """

def canUnlockAll(boxes):
    """ n number """
    key = [];

    for n in boxes[0]:
        if key == boxes[n]:
            return False;
            n - 1;
    return True;

