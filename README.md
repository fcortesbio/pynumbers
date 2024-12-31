# Python Number Theory Algorithms

This repository contains Python implementations of various number theory algorithms, with a focus on different approaches to calculate Fibonacci numbers. It also includes tools for performance measurement and detailed analysis.

## Features

- **Efficient Fibonacci Calculations**: Explore various methods for computing Fibonacci numbers, including recursive, iterative, and matrix-based approaches.
- **Performance Measurement**: A flexible `timer` function for detailed benchmarking and analysis.
- **Reports and Insights**: Detailed performance analysis and visualizations are available in the [performance report](./reports/fibonacci/performance-report.md).

## Repository Structure

```plaintext
.
├── fibonacci.py       # Fibonacci calculation methods
├── measure.py         # Timer function for benchmarking
├── prime-numbers.py   # Prime number algorithms (in progress)
├── README.md          # This file
└── reports
    └── fibonacci
        ├── average_execution_time_graph.png # Average execution time graph
        ├── average_execution_time_rawdata.json # Average execution time raw data 
        ├── extended_rawdata # Extended data results for further data analysis
        └── performance-report.md        # Detailed performance analysis
```

## Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Set up a local environment with [`conda`](https://docs.conda.io/projects/conda/en/stable/) (optional) and install the [`matplotlib`](https://matplotlib.org/stable/) library (required for data visualization).

   ```bash
   conda create env -n <env_name> python="3.10" -y --dry-run
   conda activate <env_name>
   conda install -c conda-forge matplotlib
   ```

    Or using `pip`:

   ```bash
   pip install matplotlib
   ```

3. Run the Fibonacci tests:

   ```bash
   python fibonacci.py
   ```

4. View performance insights in the [performance report](./reports/fibonacci/performance-report.md).

## License

This project is licensed under the MIT License.
