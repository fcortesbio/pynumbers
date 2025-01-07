import sys  # Required to manipulate system variables (e.g., recursion limit)
from math import sqrt  # Square root function for Binet's formula
from decimal import Decimal as dec, getcontext  # For managing high precision in Binet's formula
from functools import wraps, lru_cache  # For memoization using functools
from shorcuts import validate_index, memoize  # Importing utility functions from ../shortcuts.py

# Increase the recursion limit to allow deeper recursive calls
sys.setrecursionlimit(1500)

# Fibonacci computation methods

@validate_index
def recursion_pure(n: int) -> int:
    """Calculate the n-th Fibonacci number using pure recursion."""
    if n <= 1:  # Base case for recursion
        return n
    return recursion_pure(n - 1) + recursion_pure(n - 2)

@memoize
def recursion_memo(n: int) -> int:
    """Calculate the n-th Fibonacci number using memoized recursion.
    
    This function applies the `memoize` decorator to cache results and prevent redundant computations.
    """
    if n <= 1:  # Base case for recursion
        return n
    return recursion_memo(n - 1) + recursion_memo(n - 2)

@validate_index
def recursion_lruc(n: int) -> int:
    """Calculate the n-th Fibonacci number using recursion with `lru_cache` for memoization.
    
    The `lru_cache` decorator is applied inside the function to ensure it is detected as a valid function
    by `get_functions_from_module`. The decorator helps with caching previously computed values for efficiency.
    """
    @lru_cache(maxsize=None)  # Apply LRU caching to the inner recursion function
    def recursion(n):
        if n <= 1:  # Base case for recursion
            return n
        return recursion(n - 1) + recursion(n - 2)
    return recursion(n)

@validate_index
def iteration(n: int) -> int:
    """Calculate the n-th Fibonacci number using an iterative approach."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@validate_index
def binets_formula(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula."""
    c = 1 / sqrt(5)
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return int(round(c * (phi ** n - psi ** n)))  # Round and ensure integer output

@validate_index
def binets_formula_decimals(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula with higher precision.
    
    This approach uses the `decimal` module to provide greater precision when calculating Fibonacci numbers.
    It consumes more memory and resources but improves the accuracy for large n.
    """
    getcontext().prec = 150  # Set decimal precision
    sqrt5 = dec(sqrt(5))
    phi = (dec(1) + sqrt5) / dec(2)
    psi = (dec(1) - sqrt5) / dec(2)
    return int(round((phi ** n - psi ** n) / sqrt5))  # Round and ensure integer output

@validate_index
def matrix_exponentiation(n: int) -> int:
    """Calculate the n-th Fibonacci number using matrix exponentiation."""
    if n <= 1:
        return n

    def matrix_mul(a, b):
        """Multiply two 2x2 matrices."""
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0],
                 a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0],
                 a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    def matrix_pow(a, n):
        """Raise a 2x2 matrix to the power n."""
        if n == 1:
            return a
        elif n % 2 == 0:
            return matrix_pow(matrix_mul(a, a), n // 2)
        else:
            return matrix_mul(a, matrix_pow(matrix_mul(a, a), (n - 1) // 2))

    result = matrix_pow([[1, 1], [1, 0]], n)
    return result[0][1]

if __name__ == "__main__":
    print(recursion_pure(10))  # Example usage of the Fibonacci function