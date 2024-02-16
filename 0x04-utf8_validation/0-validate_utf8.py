#!/usr/bin/python3
"""Write a method that determines if a given data set represents a valid UTF-8 encoding."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Return: True if data is a valid UTF-8 encoding, else return False"""
    count = 0
    for dat in data:
        if count == 0:
            if dat >= 0b11110000:
                count = 3
            elif dat >= 0b11100000:
                count = 2
            elif dat >= 0b11000000:
                count = 1
            elif dat >= 0b10000000:
                return False
        else:
            if dat < 0b10000000 or dat >= 0b11000000:
                return False
            count -= 1

    return count == 0