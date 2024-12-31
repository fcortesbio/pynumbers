import sys
from measure import timer  # Decorator for measuring execution times
from math import sqrt
from functools import lru_cache  # Least Recently Used cache for improved performance in recursive Fibonacci
from decimal import Decimal as dec, getcontext
import matplotlib.pyplot as plt #! pip instal matplotlib
import json # to store results in a json file

sys.setrecursionlimit(1500) # Increase recursion limit 

invalid_input_msg = "Input must be a non-negative integer"

@lru_cache(maxsize=None)
def fibo_recs(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using recursion with memoization.

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If the input is not a non-negative integer.
    
    Notes:
        - Utilizes the @lru_cache decorator to store results of previous computations,
          significantly improving performance over naive recursion.
        - Time complexity: O(n).
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    return n if n in (0, 1) else fibo_recs(n - 1) + fibo_recs(n - 2)

def fibo_iter(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using an iterative approach.

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If the input is not a non-negative integer.

    Notes:
        - Efficient for large inputs, avoiding the overhead of recursion.
        - Time complexity: O(n).
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibo_math(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using Binet's formula.

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If the input is not a non-negative integer.

    Notes:
        - Uses a closed-form expression involving the golden ratio.
        - May suffer from floating-point precision issues for very large n.
        - Time complexity: O(1).
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)

    c = 1 / sqrt(5)
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2

    return round(c * (phi ** n) - (psi ** n))

def fibo_decm(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using Binet's formula with Decimal for higher precision.

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If the input is not a non-negative integer.

    Notes:
        - Uses the Decimal module to mitigate floating-point precision issues.
        - Time complexity: O(1).
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(invalid_input_msg)

    getcontext().prec = 150

    c = dec(1) / dec(sqrt(5))
    phi = (dec(1) + dec(sqrt(5))) / dec(2)
    psi = (dec(1) - dec(sqrt(5))) / dec(2)

    return round(c * (phi ** n) - (psi ** n))

def fibo_matx(n: int) -> int:
    """
    Calculate the n-th Fibonacci number using matrix exponentiation.

    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If the input is not a non-negative integer.

    Notes:
        - Uses matrix multiplication and exponentiation to compute the result efficiently.
        - Time complexity: O(log n).
    """
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

if __name__ == "__main__":
    # initial experimients: 
    # n = 500  # Example input
    # repl = 1000  # Number of repetitions

    # timed_fibo_recs = timer(fibo_recs, repl)
    # timed_fibo_iter = timer(fibo_iter, repl)
    # timed_fibo_math = timer(fibo_math, repl)
    # timed_fibo_decm = timer(fibo_decm, repl)
    # timed_fibo_matx = timer(fibo_matx, repl)
    
    # print(f"{timed_fibo_recs(n) = }", "\n","-"*55, sep="")
    # print(f"{timed_fibo_iter(n) = }", "\n","-"*55, sep="")
    # print(f"{timed_fibo_matx(n) = }", "\n","-"*55, sep="")
    # print(f"{timed_fibo_math(n) = }", "\n","-"*55, sep="")
    # print(f"{timed_fibo_decm(n) = }", "\n","-"*55, sep="")

    # 
    results = {
        "fibo_recs": [],
        "fibo_iter": [],
        "fibo_math": [],
        "fibo_decm": [],
        "fibo_matx": [],
        }
    repl = 40  # Number of repetitions
    n_values = range(10, 250)  # i values from 10 to 19

    for n in n_values:
        # Apply the timer decorator to each function
        timed_fibo_recs = timer(fibo_recs, repl)
        timed_fibo_iter = timer(fibo_iter, repl)
        timed_fibo_math = timer(fibo_math, repl)
        timed_fibo_decm = timer(fibo_decm, repl)
        timed_fibo_matx = timer(fibo_matx, repl)

        # Call the timed functions and store results
        results["fibo_recs"].append(timed_fibo_recs(n))
        results["fibo_iter"].append(timed_fibo_iter(n))
        results["fibo_math"].append(timed_fibo_math(n))
        results["fibo_decm"].append(timed_fibo_decm(n))
        results["fibo_matx"].append(timed_fibo_matx(n))

    print(results)

    # Store results in a JSON file
    with open("fibonacci_results.json", "w") as f:
        json.dump(results, f, indent=4)  # Use indent for pretty formatting

    # Data visualization
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed

    for func_name, times in results.items():
        plt.plot(n_values, times, label=func_name)

    plt.xlabel("n (Input Value)")
    plt.ylabel("Average Execution Time (µs)")
    plt.title("Fibonacci Function Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()
