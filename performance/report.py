import json
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    """
    Load performance data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file containing performance data.
        
    Returns:
        dict: Parsed JSON data as a dictionary.
    """
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def plot_data(data):
    """
    Plot performance data using Seaborn.
    
    Args:
        data (dict): Performance data loaded from the JSON file.
    """
    # Extract necessary data for plotting
    function_names = list(data['results'].keys())
    all_data = []
    
    for func in function_names:
        for entry in data['results'][func]:
            all_data.append({
                'Function': func,
                'n': entry['n'],
                'Mean Time (ms)': entry['mean_time'],
                'Standard Deviation (ms)': entry['std_dev_time']
            })

    # Convert to DataFrame for plotting
    import pandas as pd
    df = pd.DataFrame(all_data)

    # Plotting using Seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='n', y='Mean Time (ms)', hue='Function')
    plt.title('Performance of Different Fibonacci Calculation Methods')
    plt.xlabel('n')
    plt.ylabel('Mean Time (ms)')
    plt.legend(title='Function')
    plt.show()
