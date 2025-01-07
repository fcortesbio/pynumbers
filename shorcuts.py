from functools import wraps
import datetime

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

def get_formatted_time():
  """
  Returns the current time in the format MMDDYY_HH.MM.
  """
  now = datetime.datetime.now()
  return now.strftime("%m%d%y_%H.%M")

# Get the formatted time string
formatted_time = get_formatted_time()
print(formatted_time)

