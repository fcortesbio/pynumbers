from measure import timer # decorator for measuring execution times
from math import sqrt 
from functools import lru_cache # ~Least Recently Used cache~. Used to improve fibo_rects performance
from decimal import Decimal as dec, getcontext

invalid_input_msg = "Input must be a non-negative integer"

@lru_cache(maxsize=None) # 
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
    
    getcontext().prec = 50 # Set precision of 50 significant numbers

    if n in (0, 1):
        return n
    
    c = dec(1) / dec(sqrt(5)) #                c = 1 ÷ √5
    phi = (dec(1) + dec(sqrt(5)))/dec(2) #     Φ = (1 + √5) ÷ 2
    psi = (dec(1) - dec(sqrt(5)))/dec(2) #     Ψ = (1 - √5) ÷ 2

    return round(c * (phi ** n) - (psi ** n))  #  f(n) = c × Φ^n × Ψ^n
    
if __name__ == "__main__":
    n = 500 
     # Example input
    repl = 1000  # Number of repetitions

    # Apply the timer decorator to each function
    timed_fibo_recs = timer(fibo_recs, repl)
    timed_fibo_iter = timer(fibo_iter, repl)
    timed_fibo_math = timer(fibo_math, repl)

    # Call the timed functions
    
    print(timed_fibo_recs(n))
    print(timed_fibo_iter(n))
    print(timed_fibo_math(n))
    