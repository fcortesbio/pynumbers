import sys  # Required for manipulating system variables
# from timer import timer  # execution times benchmarking
from math import sqrt  # Square root
from functools import lru_cache  # Memoization for improving recursive performance
from decimal import Decimal as dec, getcontext

# Increase recursion limit
sys.setrecursionlimit(1500)

# Global variable for input validation
invalid_input_msg = "Input must be a non-negative integer"

# Fibonacci computation methods
def fibo_recs(n: int) -> int:
    """Calculate the n-th Fibonacci number using pure recursion."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    return n if n in (0, 1) else fibo_recs(n - 1) + fibo_recs(n - 2)

@lru_cache(maxsize=None)
def fibo_lruc(n: int) -> int:
    """Calculate the n-th Fibonacci number using recursion with memoization."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    return n if n in (0, 1) else fibo_lruc(n - 1) + fibo_lruc(n - 2)

def fibo_iter(n: int) -> int:
    """Calculate the n-th Fibonacci number using an iterative approach."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibo_math(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    c = 1 / sqrt(5)
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return round(c * (phi ** n) - (psi ** n))

def fibo_decm(n: int) -> int:
    """Calculate the n-th Fibonacci number using Binet's formula with higher precision."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    getcontext().prec = 150
    c = dec(1) / dec(sqrt(5))
    phi = (dec(1) + dec(sqrt(5))) / dec(2)
    psi = (dec(1) - dec(sqrt(5))) / dec(2)
    return round(c * (phi ** n) - (psi ** n))

def fibo_matx(n: int) -> int:
    """Calculate the n-th Fibonacci number using matrix exponentiation."""
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
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