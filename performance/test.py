import importlib
import inspect
import argparse
import os
import json
from typing import Callable
from shorcuts import get_formatted_time as time_now
from performance.timer import timer

def get_functions_from_module(module_path):
    try:
        module_name = os.path.basename(module_path) + '.functions'
        module = importlib.import_module(module_name)
        return [obj for name, obj in inspect.getmembers(module) if inspect.isfunction(obj) and obj.__module__ == module_name]
    except ModuleNotFoundError:
        print(f'Module "functions.py" not found in "{module_path}".')
        return []

def run_performance_test(functions: Callable, repetitions: int, start: int, end: int, steps: int):
    results = {}
    for func in functions:
        results[func.__name__] = []  # Initialize the list for each function
        print(f'Running {func.__name__} ...')
        for n in range(start, end, steps):
            try:
                timed_func = timer(lambda: func(n), repetitions)
                results[func.__name__].append({
                    'n': n,
                    'mean_time': timed_func['mean_time'],
                    'std_dev_time': timed_func['std_dev_time']
                })
            except ValueError as ve:
                print(f'Error for n={n}: {ve}')
                results[func.__name__].append({
                    'n': n, 
                    'error': str(ve)
                })
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run performance tests on module functions.')
    parser.add_argument('--source', '-s', required=True, help='Path to the module directory')
    parser.add_argument('--repetitions', '-r', type=int, default=10, help='Number of repetitions for each test')
    parser.add_argument('--output', '-o', default=f'perf_test_{time_now()}.json', help='Output file for results')
    parser.add_argument('--start', type=int, default=0, help='Initial n value for iteration')
    parser.add_argument('--end', type=int, default=10, help='Last n value for iteration')
    parser.add_argument('--steps', type=int, default=1, help='Steps for iteration')
    args = parser.parse_args()

    try: 
        repetitions, start, end, steps = args.repetitions, args.start, args.end, args.steps
        if start < 0 or end <= start or steps <= 0:
            raise ValueError("Invalid range for start, end, or steps")
    except ValueError as ve:
        print(f"Argument error: {ve}")
        exit(1)

    functions = get_functions_from_module(args.source)
    output = args.output
    
    if functions:
        print('Functions found:')
        for func in functions:
            print(f'- {func.__name__}')
        results = run_performance_test(functions, repetitions, start, end, steps)
        with open(output, 'w') as outfile:
            json.dump(results, outfile, indent=4)
        print(f'Performance data saved to: {output}')
    else:
        print('No functions to test')
