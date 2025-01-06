import sys
import os

# Add the parent directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from fibonacci import fibo_recs, fibo_lruc, fibo_iter, fibo_math, fibo_decm, fibo_matx
from .timer import timer

import matplotlib.pyplot as plt  # Visualization library
import json  # To save results in a file

results = {
    "fibo_recs": [],
    "fibo_lruc": [],
    "fibo_iter": [],
    "fibo_math": [],
    "fibo_decm": [],
    "fibo_matx": [],
}

repl = 10  # Number of repetitions per test
n_values = range(2, 150)  # Fibonacci input values to test

for n in n_values:
    try:
        if n <= 10: # max value for pure recursion
            timed_fibo_recs = timer(lambda: fibo_recs(n), repl)
            results["fibo_recs"].append(timed_fibo_recs["mean_time"])
        else: 
            results["fibo_recs"].append(None) # Skip pure recursion if n>35

        # Measure execution time for each function
        # timed_fibo_recs = timer(lambda: fibo_recs(n), repl)
        timed_fibo_lruc = timer(lambda: fibo_lruc(n), repl)
        timed_fibo_iter = timer(lambda: fibo_iter(n), repl)
        timed_fibo_math = timer(lambda: fibo_math(n), repl)
        timed_fibo_decm = timer(lambda: fibo_decm(n), repl)
        timed_fibo_matx = timer(lambda: fibo_matx(n), repl)

        # Append average execution times
        # results["fibo_recs"].append(timed_fibo_recs["mean_time"])
        results["fibo_lruc"].append(timed_fibo_lruc["mean_time"])
        results["fibo_iter"].append(timed_fibo_iter["mean_time"])
        results["fibo_math"].append(timed_fibo_math["mean_time"])
        results["fibo_decm"].append(timed_fibo_decm["mean_time"])
        results["fibo_matx"].append(timed_fibo_matx["mean_time"])
    except ValueError as ve:
        print(f"Error for n={n}: {ve}")
        for key in results:
            results[key].append(None)


# Save results to a JSON file
with open("av_et_rawdata2.json", "w") as f:
    json.dump(results, f, indent=4)

# Data Visualization
plt.figure(figsize=(12, 8))
for func_name, times in results.items():
    valid_times = [t for t in times if t is not None]
    valid_n = [n for n, t in zip(n_values, times) if t is not None]
    plt.plot(valid_n, valid_times, label=func_name)

plt.xlabel("n (Input Value)")
plt.ylabel("Average Execution Time (μs)")
plt.title("Fibonacci Function Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()
