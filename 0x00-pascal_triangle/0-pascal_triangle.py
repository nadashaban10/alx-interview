#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows using the nCr formula.

    Args:
            n: An integer representing the number of rows in the triangle.

    Returns:
            A list of lists containing the Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        # Use nCr formula to calculate each element in the row
        for j in range(i + 1):
            ncr = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(ncr)
        triangle.append(row)
    return triangle


def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
