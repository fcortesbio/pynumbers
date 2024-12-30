from time import perf_counter as performance
from typing import Callable

def func_timer(func: Callable, replics: int = 10) -> Callable:
    """
    Decorator to measure execution time of a function.

    Args: 
        func: The function to be timed.
        replics: Number of times the function is executed (default: 10).

    Returns: 
        A wrapped function that measures and prints the average execution time.
    """
    def wrapper(*args, **kwargs):
        samples = []
        for _ in range(replics):
            start_time = performance()
            result = func(*args, **kwargs)
            end_time = performance()
            samples.append(end_time - start_time)
        average = sum(samples) / replics
        print(f"Function name: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        print(f"Average execution time: {average:.6f} seconds")
        return result
    return wrapper
