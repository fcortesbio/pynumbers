import sys  # Required for manipulating system variables
from math import sqrt  # Square root for Binet's formula
from decimal import Decimal as dec, getcontext  # For decimal management in Binet's formula with increased precision
from functools import wraps, lru_cache

# Increase recursion limit
sys.setrecursionlimit(1500)

# Decorator for input validation
def validate_index(func):
    """Validates that the first argument to a function is a non-negative integer.

    This decorator checks if the first positional argument (`n`) passed to the 
    decorated function is a non-negative integer. If not, it raises a ValueError.

    Args:
        func (Callable): The function to be decorated.

    Raises:
        ValueError: If the first argument to the function is not a non-negative integer.

    Returns:
        Callable: The decorated function.
    """
    invalid_input_msg = "Input must be a non-negative integer."
    @wraps(func)
    def wrapper(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError(invalid_input_msg)
        return func(n)
    return wrapper

def memoize(func):
    """Memoizes a function.

    This decorator caches the results of a function based on its arguments. 
    If the function is called again with the same arguments, the cached result 
    is returned instead of recomputing.

    Args:
        func (Callable): The function to be memoized.

    Returns:
        Callable: The memoized function.
    """
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper     


# Fibonacci computation methods
@validate_index
def pure_recursion(n: int) -> int:
    """Calculate the n-th Fibonacci number using pure recursion.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 1:  # Base case for recursion
        return n
    return pure_recursion(n - 1) + pure_recursion(n - 2)

@memoize
def memoized_recursion(n: int) -> int: 
    """Calculate the n-th Fibonacci number using memoized recursion.

    This function uses the `memoize` decorator to cache results and avoid 
    redundant computations.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
    return pure_recursion(n)
    
@lru_cache(maxsize=None)
def memoized_lru_cache_recursion(n: int) -> int:
    """Calculate the n-th Fibonacci number using recursion with lru_cache.

    This function uses the `lru_cache` decorator from `functools` for 
    memoization.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
    return pure_recursion(n)

@validate_index
def iteration(n: int) -> int:
    """Calculate the n-th Fibonacci number using an iterative approach.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@validate_index
def binets_formula(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
    c = 1 / sqrt(5)
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return int(round(c * (phi ** n - psi ** n)))  # Ensure integer output

@validate_index
def binets_formula_decimals(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula with higher precision.

    This function uses the `decimal` module to improve accuracy for large values of `n`.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
    getcontext().prec = 150  # Set decimal precision
    sqrt5 = dec(sqrt(5))
    phi = (dec(1) + sqrt5) / dec(2)
    psi = (dec(1) - sqrt5) / dec(2)
    return int(round((phi ** n - psi ** n) / sqrt5))  # Ensure integer output

@validate_index
def matrix_exponentiation(n: int) -> int:
    """Calculate the n-th Fibonacci number using matrix exponentiation.

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The n-th Fibonacci number.
    """
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