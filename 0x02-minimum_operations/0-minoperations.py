#!/usr/bin/python3

"""
This script defines a method for performing operations on a single
character 'H' with two operations: Copy All and Paste.
Given a number 'n', the goal is to calculate the minimum number of
operations needed to result in exactly 'n' occurrences of 'H'.

Module Docstring:
-----------------
Has a single character H with two operations: Copy All and Paste
Give number n, write a method that calculates operations to result
in exactly n H.
Prototype: def minOperations(n)
Return an integer
if n is impossible to achieve, return 0
"""

def minOperations(n):
    """
    Single character H
    Fewest number of operations

    Parameters:
    -----------
    n : int
        The target number of occurrences of 'H'.

    Returns:
    --------
    int
        The minimum number of operations required to achieve
        'n' occurrences of 'H'.
        Returns 0 if it is impossible to achieve 'n'.
    """

    # Base case: If n is less than or equal to 1, no operations are needed.
    if n <= 1:
        return 0

    # Initialize variables
    numbr, index, operations = n, 2, 0

    # Iterate until numbr is reduced to 1
    while numbr > 1:
        # Check if numbr is divisible by index
        if numbr % index == 0:
            numbr = numbr / index
            operations = operations + index
        else:
            # If not divisible, increment index
            index += 1

    return operations
