#!/usr/bin/python3
def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n 'H' characters.

    Args:
    - n (int): The target number of 'H' characters.

    Returns:
    - int: The minimum number of operations. If n is impossible to achieve, return 0.
    """

    if n <= 1:
        return 0