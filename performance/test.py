import importlib
import inspect
import argparse
import os

def get_functions_from_module(module_path):
    """
    Imports a module (functions.py inside a given path) and returns a list of its functions,
    excluding decorators and imported functions.

    Args:
        module_path (str): The path to the directory containing functions.py.

    Returns:
        list: A list of functions from the module.
    """
    try:
        # Construct the full module name
        module_name = os.path.basename(module_path) + ".functions"

        # Import the module
        module = importlib.import_module(module_name)

        functions = []
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and obj.__module__ == module_name:
                functions.append(obj)
        return functions
    except ModuleNotFoundError:
        print(f"Module 'functions.py' not found in '{module_path}'.")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get functions from a module.")
    parser.add_argument("--source", "--src", "-s", required=True, help="Path to the module directory")
    args = parser.parse_args()

    functions = get_functions_from_module(args.source)

    if functions:
        print("Functions found:")
        for func in functions:
            print(f"- {func.__name__}")