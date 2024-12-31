# Python Number Theory Algorithms

This repository contains a collection of Python implementations for common number theory algorithms and problems. It currently includes various approaches for calculating Fibonacci numbers, along with a performance measurement decorator.

## Fibonacci Numbers

The [`fibonacci.py`](./fibonacci.py) file provides several functions for calculating Fibonacci numbers:

* `fibo_recs(n)`: Recursive implementation (optimized with memoization).
* `fibo_iter(n)`: Iterative implementation.
* `fibo_math(n)`: Direct calculation using Binet's formula (with standard `math` module).
* `fibo_decm(n)`: Direct calculation using Binet's formula (with `Decimal` for higher precision).
* `fibo_matx(n)`: Calculation using matrix exponentiation.

Each function has different strengths, with performance measured using the `timer` decorator.

## Timer Decorator

The `measure.py` file contains the `timer` decorator, which can be used to measure the average execution time of a function over multiple runs:

```python
from measure import timer

@timer(func, repetitions)
def my_function(...):
    # ...
```

The decorator prints the average execution time in microseconds and helps benchmark your functions efficiently.

## Experiments and Takeaways

In my experiments, I compared various Fibonacci calculation techniques, optimizing for both performance and accuracy. Below are some key observations based on 1000 runs with `n = 500`:

```plaintext
Average Execution time for fibo_recs: 0.395896 µs
timed_fibo_recs(n) = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
-------------------------------------------------------

Average Execution time for fibo_iter: 18.591298 µs
timed_fibo_iter(n) = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
-------------------------------------------------------

Average Execution time for fibo_matx: 9.842015 µs
timed_fibo_matx(n) = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
-------------------------------------------------------

Average Execution time for fibo_math: 0.602354 µs
timed_fibo_math(n) = 139423224561700228711116466856628305532793116368214754989670287848858933271320300167384646404854199091200
-------------------------------------------------------

Average Execution time for fibo_decm: 16.170770 µs
timed_fibo_decm(n) = 139423224561700213746098001335981127141975995461170052039273556102288684192412160681502933644886486015484
-------------------------------------------------------
```

**Key Takeaways**:

* **Memoization**: The `fibo_recs` function is significantly optimized through memoization, reducing redundant calculations and performing very well despite being recursive.
* **Iterative vs. Mathematical**: The iterative approach (`fibo_iter`) outperforms the mathematical calculation for large Fibonacci numbers, while the mathematical approach (`fibo_math`) is generally slower due to the overhead of floating-point operations.
* **Precision**: For very large Fibonacci numbers, the `Decimal` module with higher precision ensures more accurate results but at the cost of increased execution time.
* **Performance vs. Accuracy**: There's a balance between performance and accuracy. While `Decimal` improves accuracy, it increases the time complexity.
* **Floating-Point Limitations**: Binet's formula and floating-point calculations can lead to precision issues for very large Fibonacci numbers.

## Future Plans

In the future, this repository will expand to cover other number theory problems, such as:

* Prime number generation and primality testing
* Factorial calculations
* Greatest common divisor (GCD) and least common multiple (LCM)
* And more!

## How to Use

1. Clone the repository.
2. Ensure Python is installed, and set up a virtual environment if necessary.
3. Run the `fibonacci.py` file to see the Fibonacci implementations and performance benchmarks.
4. Use the `timer` decorator from `measure.py` to measure the execution time of your own functions.

## Contributing

Contributions are welcome! If you'd like to add new algorithms, improve existing ones, or suggest other number theory problems to include, feel free to submit a pull request.
