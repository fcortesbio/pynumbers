from time import perf_counter as performace
from typing import Callable

def timer(func, repl):
    """
    Decorator to measure the average execution time of a function over multiple runs.

    Args:
        func: The function to be timed.
        repl: The number of times to execute the function (default is 1).

    Returns:
        A wrapped function that measures and prints the average execution time in milliseconds.
    """

    def wrapper(*args):
        start_time = performace()
        for _ in range(repl):
            func(*args)
        end_time = performace()
        average = (end_time - start_time) / repl # performance returns time in seconds 
        average_microseconds = average * 1e6 # convert to microseconds

        print(f"Average Execution time for {func.__name__}: {average_microseconds:.6f} µs.")
        return func(*args)
    return wrapper
