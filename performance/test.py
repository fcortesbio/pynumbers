import importlib
import inspect
import argparse
import os
import json
from shorcuts import get_formatted_time as time_now
from performance.timer import timer


def get_functions_from_module(module_path):
    try:
        module_name = os.path.basename(module_path) + ".functions"
        module = importlib.import_module(module_name)
        return [obj for name, obj in inspect.getmembers(module) if inspect.isfunction(obj) and obj.__module__ == module_name]      

    except ModuleNotFoundError:
        print(f"Module 'functions.py' not found in '{module_path}'.")
        return []

def run_performance_test(functions, repetitions):
    results = {}
    for func in functions:
        print(f"Running {func.__name__}...")
        result = timer(func, repetitions, store_samples=True)
        results[func.__name__] = result
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run performance tests on module functions.")
    parser.add_argument("--source", "-s", required=True, help="Path to the module directory")
    parser.add_argument("--repetitions", "-r", type=int, default=10, help="Number of repetitions for each test")
    parser.add_argument("--output", "-o", default=f"perf_test_{time_now()}.json", help="Output file for results")
    args = parser.parse_args()

    functions = get_functions_from_module(args.source)

    if functions:
        results = run_performance_test(functions, args.repetitions)
        with open("args.output", "w") as outfile:
            json.dump(results, outfile, indent=4)
        print(f"Performance data saved to: {args.output}")
        
    else:
        print("No functions to test")