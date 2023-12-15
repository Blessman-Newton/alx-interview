#!/usr/bin/python3
""" Minimum Operations
    """

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    current = 1  # Current number of characters in the file
    clipboard = 1  # Characters in the clipboard

    while current < n:
        if n % current == 0:
            clipboard = current
        current += clipboard
        operations += 1

    return operations
