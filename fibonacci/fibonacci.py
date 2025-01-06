import sys  # Required for manipulating system variables
from math import sqrt  # Square root for Binnet's formula
from decimal import Decimal as dec, getcontext # for decimal manage in Binnet's formula with increased precision 
from functools import wraps
from functools import lru_cache  # Memoization using lru_cache from functools

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
    invalid_input_msg = "Input must be a non-negative integer"
    @wraps(func)
    def wrapper(n):  # Only 'n' is needed
        if not isinstance(n, int) or n < 0:
            raise ValueError(invalid_input_msg)
        return func(n)
    return wrapper

def memoize(func):
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
    return n if n in (0, 1) else pure_recursion(n - 1) + pure_recursion(n - 2)
        
@memoize
def memoized_recursion(n: int) -> int: 
    """"""
    return pure_recursion(n)
    
@lru_cache
def memoized_lruc_recursion(n: int) -> int:
    """"""
    return pure_recursion(n)

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
    return round(c * (phi ** n) - (psi ** n))

@validate_index
def binets_formula_decimals(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula with higher precision."""
    getcontext().prec = 150
    c = dec(1) / dec(sqrt(5))
    phi = (dec(1) + dec(sqrt(5))) / dec(2)
    psi = (dec(1) - dec(sqrt(5))) / dec(2)
    return round(c * (phi ** n) - (psi ** n))

@validate_index
def matrix_exponentiation(n: int) -> int:
    """Calculate the n-th Fibonacci number using matrix exponentiation."""
    if n in (0, 1):
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
