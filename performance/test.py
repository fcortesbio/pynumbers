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
        print(f'Module `functions.py` not found in "{module_path}".')
        return []

def run_performance_test(functions: Callable, repetitions: int, start: int, end: int, steps: int, ex_time_limit: int):
    results = {}
    for func in functions:
        print(f'Running {func.__name__} ...')
        results[func.__name__] = []
        for n in range(start, end, steps):
            try:
                timed_func = timer(lambda: func(n), repetitions)
                if timed_func['mean_time'] > ex_time_limit:  
                    print(f'Skipping {func.__name__} for n={n} as it exceeds the time limit of {ex_time_limit} ms.')
                    break  # Skip subsequent values of `n`
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
    parser.add_argument('--source', '-S', required=True, help='Path to the module directory')
    parser.add_argument('--repetitions', '-r', type=int, default=10, help='Number of repetitions for each test')
    parser.add_argument('--output', '-o', default=f'perf_test_{time_now()}.json', help='Output file for results')
    parser.add_argument('--start', '-st', type=int, default=0, help='Initial n value for iteration')
    parser.add_argument('--end', '-e', type=int, default=10, help='Last n value for iteration')
    parser.add_argument('--steps', '-stp', type=int, default=1, help='Steps for iteration')
    parser.add_argument('--ms_limit', '-l', type=int, default=200, help='Execution time limit in ms')
    args = parser.parse_args()

    # Ensure the reports folder exists
    reports_folder = 'reports'
    os.makedirs(reports_folder, exist_ok=True)
    output_path = os.path.join(reports_folder, args.output)

    functions = get_functions_from_module(args.source)
    repetitions, start, end, steps, ms_limit = args.repetitions, args.start, args.end, args.steps, args.ms_limit

    if functions:
        print('Functions found:')
        for func in functions:
            print(f'- {func.__name__}')
        results = run_performance_test(functions, repetitions, start, end, steps, ms_limit)
        
        # Add user prompt and parameters to the output data
        output_data = {
            'parameters': {
                'source': args.source,
                'output': args.output,
                'repetitions': args.repetitions,
                'start': args.start,
                'end': args.end,
                'steps': args.steps,
                'ms_limit': args.ms_limit
            },
            'results': results
        }
        
        with open(output_path, 'w') as outfile:
            json.dump(output_data, outfile, indent=4)
        print(f'Performance data saved to: {output_path}')
        
        plot = input(f"Generate plot for {args.source}?")
        if plot in ("y", "yes"):
            pass
        else: 
            pass
        
    else:
        print('No functions to test')