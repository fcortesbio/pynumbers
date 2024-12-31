def timer(func, repl, store_samples=False):
    """
    Measure execution time of a function over multiple runs, with optional sample storage.

    Args:
        func: Function to time.
        repl: Number of repetitions.
        store_samples (bool): Whether to store individual execution time samples.

    Returns:
        dict: Contains mean, variance, standard deviation, and optionally raw samples.
    """
    samples = []
    for _ in range(repl):
        start_time = performace()
        func()
        end_time = performace()
        samples.append((end_time - start_time) * 1e6)  # Convert to microseconds

    mean = sum(samples) / repl
    variance = sum((x - mean) ** 2 for x in samples) / repl
    std_dev = variance ** 0.5

    result = {
        "mean": mean,
        "variance": variance,
        "std_dev": std_dev,
    }

    if store_samples:
        result["samples"] = samples

    return result
