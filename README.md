# Python Number Theory Algorithms

This learning repository contains a collection of Python implementations for common number theory algorithms and problems. Currently, it focuses on various approaches for calculating Fibonacci numbers, along with a performance measurement decorator.

## Timer Decorator

The [`measure.py`](./measure.py) file contains the `@timer` decorator, which measures the average execution time of a function over multiple runs:

```python
from measure import timer

@timer(func, repetitions)
def my_function(...):
    # ...
```

This decorator prints the average execution time in microseconds, helping you benchmark your functions efficiently.

## Fibonacci Numbers

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence continues infinitely, like this:

$$ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \dots $$

This simple pattern has fascinating connections to mathematics, biology, computer science, and even art.

Common methods to calculate Fibonacci numbers include iterative and recursive approaches. While the iterative method is generally more resource-efficient, recursion is often preferred for its simplicity. However, recursion can be less efficient and prone to stack overflow due to repeated function calls. 

### Binet’s Formula

[Binet's formula](https://en.wikipedia.org/wiki/Fibonacci_sequence#Closed-form_expression) is an explicit solution for finding the \(n\)-th Fibonacci number. I hypothesized that using this formula, which requires fewer steps than recursion or iteration, would reduce computation time for large numbers. Initially, a [JavaScript program](https://github.com/fcortesbio/algorithms/blob/main/fibonacci.js) (running in a Node.js environment) confirmed my hypothesis, with the explicit formula performing better than the pure recursive method.

However, my tests in Python yielded different results. Surprisingly, the explicit formula approach was slower than the iterative method. For smaller Fibonacci numbers, the explicit formula performed well, but larger numbers introduced precision loss due to floating-point operations.

### Memoization for Optimization

During my research, I found that **memoization** can significantly speed up recursive functions. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again, avoiding redundant calculations.

In Python, the `@lru_cache` decorator from the [`functools`](https://docs.python.org/3/library/functools.html) module is an easy and efficient way to implement memoization. I used this in the final recursive function to improve performance.

Additionally, I used Python's [`decimal`](https://docs.python.org/3/library/decimal.html) module to control the precision of floating-point calculations when using Binet's formula, in an attempt to reduce information loss during Fibonacci number computations.

### Experiments and Takeaways

In my experiments, I compared various Fibonacci calculation methods, optimizing for both performance and accuracy. Below are the different approaches used, with performance measured using the `timer` decorator:

The [`fibonacci.py`](./fibonacci.py) file includes several functions for calculating Fibonacci numbers:

* [`fibo_recs(n)`](./fibonacci.py#L12): Recursive implementation (optimized with memoization).
* [`fibo_iter(n)`](./fibonacci.py#L34): Iterative implementation.
* [`fibo_math(n)`](./fibonacci.py#L58): Direct calculation using Binet's formula (with the `math` module).
* [`fibo_decm(n)`](./fibonacci.py#L85): Direct calculation using Binet's formula (with the `decimal` module for higher precision).
* [`fibo_matx(n)`](./fibonacci.py#L113): Matrix exponentiation approach.

The following results were observed from 1000 runs with `n = 500`, but I would like to encourage you to reproduce the experiment and try as many variants as needed to satisfy your curiosity:

``` python3.13 fibonacci.py
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

- **Memoization**: The `fibo_recs` function performs much better with memoization, significantly reducing redundant calculations, making it an efficient recursive approach. While results for recursion without memoization are not included here because its high computational cost limited the number of samples I could test—my laptop struggled with any values of $n >= 50$, notably, the memoized version consistently outperformed all other approaches in every experiment.  

- **Iterative vs. Mathematical**: The iterative approach (`fibo_iter`) generally outperforms the mathematical calculation (`fibo_math`) for large Fibonacci numbers due to reduced overhead.

- **Precision**: For very large Fibonacci numbers, the `decimal` module ensures higher accuracy in calculations but at the cost of increased execution time.

- **Performance vs. Accuracy**: There's a trade-off between performance and accuracy. Using `Decimal` improves precision but increases computation time.

- **Floating-Point Limitations**: Floating-point arithmetic can lead to precision issues when using Binet's formula for very large Fibonacci numbers.

## Future Plans

The repository will be expanded to cover additional number theory problems, such as:

- Prime number generation and primality testing
- Factorial calculations
- Greatest common divisor (GCD) and least common multiple (LCM)
- And more!

## How to Use

1. Clone the repository.
2. Ensure that Python is installed and set up a virtual environment if necessary.
3. Run the [`fibonacci.py`](./fibonacci.py) file to see the Fibonacci implementations and their performance benchmarks.
4. Use the `@timer` decorator from [`measure.py`](./measure.py) to measure the execution time of your own functions.

## Contributing

Contributions are welcome! If you'd like to add new algorithms, improve existing ones, or suggest other number theory problems to include, feel free to submit a pull request.