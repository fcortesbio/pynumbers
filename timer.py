from time import perf_counter
from typing import Callable, Dict, Any
import statistics

def timer(func: Callable, repl: int, store_samples: bool = False, check_output: bool = False, *args, **kwargs) -> Dict[str, Any]:
    """
    Measure execution time of a function over multiple runs and optionally evaluate output variance.

    Args:
        func: Function to time.
        repl: Number of repetitions.
        store_samples (bool): Whether to store individual execution time samples.
        check_output (bool): Whether to analyze variance in the function's output.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        dict: Contains mean, variance, standard deviation for execution time, and optionally:
              - raw execution time samples,
              - output variance, standard deviation, and list of outputs.
    """
    time_samples = []
    outputs = []

    for _ in range(repl):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()

        time_samples.append((end_time - start_time) * 1e6)  # Convert to microseconds
        if check_output:
            outputs.append(result)

    # Execution time statistics
    mean_time = statistics.mean(time_samples)
    std_dev_time = statistics.stdev(time_samples)
    variance_time = std_dev_time ** 2

    # Output statistics (if enabled)
    result = {
        "mean_time": mean_time,
        "variance_time": variance_time,
        "std_dev_time": std_dev_time,
    }

    if store_samples:
        result["time_samples"] = time_samples

    if check_output:
        mean_output = statistics.mean(outputs)
        std_dev_output = statistics.stdev(outputs) if len(outputs) > 1 else 0.0
        variance_output = std_dev_output ** 2

        result.update({
            "mean_output": mean_output,
            "variance_output": variance_output,
            "std_dev_output": std_dev_output,
            "outputs": outputs if store_samples else None,  # Store outputs if requested
        })

    return result
