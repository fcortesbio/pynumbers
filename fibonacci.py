from math import sqrt
from functools import lru_cache # used memoization to improve fibo_rects performance
from measure import func_timer as timer

invalid_input_msg = "Input must be a non-negative integer"

@lru_cache(maxsize=None)
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
    c = 1 / sqrt(5)
    phi = (1 + sqrt(5))/2
    psi = (1 - sqrt(5))/2

    return round(c * (phi ** n) - (psi ** n))
   

if __name__ == "__main__":
    test_numbers = [0, 1, 5, 10, 20]
    for n in test_numbers:
        print(f"n = {n}")
        print(f"Recursive: {fibo_recs(n)}")
        print(f"Iterative: {fibo_iter(n)}")
        print(f"Math: {fibo_math(n)}")
        print("-" * 20)