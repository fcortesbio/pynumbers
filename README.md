# Python Number Theory Algorithms

This repository contains a collection of Python implementations for common number theory algorithms and problems. It currently includes various approaches for calculating Fibonacci numbers, along with a performance measurement decorator.

## Fibonacci Numbers

The `fibonacci.py` file provides several functions for calculating Fibonacci numbers:

* `fibo_recs(n)`: Recursive implementation (optimized with memoization).
* `fibo_iter(n)`: Iterative implementation.
* `fibo_math(n)`:  Direct calculation using Binet's formula (with standard `math` module).
* `fibo_decm(n)`:  Direct calculation using Binet's formula (with `Decimal` for higher precision).
* `fibo_matx(n)`:  Calculation using matrix exponentiation.

## Timer Decorator

The `measure.py` file contains the `timer` decorator. This decorator can be used to measure the average execution time of a function over multiple runs.

```python
from measure import timer

@timer(func, repetitions)
def my_function(...):
    # ...
```

## Experiments and Takeaways

I've made several comparisons and adjustments while developing this experiment, varying among diffent approaches, techniques and optimizations to get the $n$ number in the Fibonacci series. I finally opted for keeping a number of them as separate functions and use the @timer to help illustrating the overall performance of each one.

Experiments were conducted to compare the performance and accuracy of different Fibonacci implementations. The following output is for 1000 replics and n=500; but I encourage you to try different values as needed to satisfy your curiosity.

``` python fibonacci.py

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

Here are some key takeaways:

* **Memoization:** The `fibo_recs` function, despite being recursive, performs very well due to memoization, which significantly reduces redundant calculations.

* **Iterative vs. Mathematical:** The iterative approach (`fibo_iter`) is generally more efficient than the direct mathematical calculation using Binet's formula for large Fibonacci numbers.
* **Precision:**  For extremely large Fibonacci numbers, using the `Decimal` module with higher precision is necessary to maintain accuracy in the mathematical calculations.
* **Performance vs. Accuracy:** There's often a trade-off between performance and accuracy. Using higher precision with `Decimal` can improve accuracy but also increases execution time.
* **Number of Operations vs. Cost:** The overall performance depends not only on the number of operations but also on the cost of each operation. A few expensive operations (like multiplications/divisions with large numbers) can be slower than many cheaper operations (like additions).
* **Floating-Point Limitations:**  Calculations involving floating-point numbers can have inherent precision issues, especially with division and very large or very small numbers.

## Future Plans

This repository will be expanded to include modules for other number theory problems, such as:

* Prime number generation and primality testing
* Factorial calculations
* Greatest common divisor (GCD) and least common multiple (LCM)
* And more!

## How to Use

1. Clone the repository.
2. Run the `fibonacci.py` file to see the Fibonacci implementations and their performance comparisons.
3. Use the `timer` decorator from `measure.py` to measure the execution time of your own functions.

## Contributing

Contributions are welcome! If you'd like to add new algorithms, improve existing ones, or suggest other number theory problems to include, feel free to submit a pull request.
