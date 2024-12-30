from measure import timer # decorator for measuring execution times
from math import sqrt
from functools import lru_cache # used memoization to improve fibo_rects performance


invalid_input_msg = "Input must be a non-negative integer"

# @lru_cache(maxsize=None)
def fibo_recs(n: int) -> int:
    """
    Returns the 'n' number of the Fibonacci series using recursion. 
    Efficiency improved through memoization 
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    return n if n in (0, 1) else fibo_recs(n - 1) + fibo_recs(n - 2)
    
def fibo_iter(n : int) -> int:
    """
    Returns the 'n' number of the Fibonaci series obtained from iterative additions.
    Efficient for large inputs.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b 
    return a

def fibo_math(n: int) -> int:
    """
    Returns the 'n' number in the Fibonacci sereis using Binnet's formula.
    Note: Precision issues may arise for very large numbers 
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    
    if n in (0, 1):
        return n
    
    c, phi, psi = 1 / sqrt(5), (1 + sqrt(5))/2, (1 - sqrt(5))/2
    return round(c * (phi ** n) - (psi ** n))
   
if __name__ == "__main__":
    n = 10  # Example input
    repl = 1000  # Number of repetitions

    # Apply the timer decorator to each function
    timed_fibo_recs = timer(fibo_recs, repl)
    timed_fibo_iter = timer(fibo_iter, repl)
    timed_fibo_math = timer(fibo_math, repl)

    # Call the timed functions
    
    print(timed_fibo_recs(n))
    print(timed_fibo_iter(n))
    print(timed_fibo_math(n))
    