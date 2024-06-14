#!/usr/bin/python3
'''
Minimum Operations Coding Problem

'''


def minOperations(n):
    '''Calculate the fewest number of operations
    needed to result in exactly n 'H' characters in a text file.
    Parameters:
    n (int): The target number of 'H' characters.
    Returns:
    int: The minimum number of operations
    '''
    # If n is less than or equal to 1 =>>
    # it's impossible to achieve the target, return 0
    if n <= 1:
        return 0
    operations = 0
    # Start with the smallest prime factor
    factor = 2

    # Check for factors
    while (factor**2 <= n):
        if n % factor == 0:
            # Add the factor to the operations count
            operations += factor
        # Update n by dividing it by the current factor
            n //= factor
        else:
            factor += 1

    # If n>1, it means n is a prime number greater than its square root.
    if n > 1:
        operations += n
    # Return the total number of operations
    return operations
