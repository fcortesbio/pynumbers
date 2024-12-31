# Fibonacci Numbers

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence continues infinitely, like this:

$$ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \dots $$

This simple pattern has fascinating connections to mathematics, biology, computer science, and even art.

Common methods to calculate Fibonacci numbers include iterative and recursive approaches. While the iterative method is generally more resource-efficient, recursion is often preferred for its simplicity. However, recursion can be less efficient and prone to stack overflow due to repeated function calls. 



## Background

### Binet’s Formula

[Binet's formula](https://en.wikipedia.org/wiki/Fibonacci_sequence#Closed-form_expression) is an explicit solution for finding the \(n\)-th Fibonacci number. I hypothesized that using this formula, which requires fewer steps than recursion or iteration, would reduce computation time for large numbers. Initially, a [JavaScript program](https://github.com/fcortesbio/algorithms/blob/main/fibonacci.js) (running in a Node.js environment) confirmed my hypothesis, with the explicit formula performing better than the pure recursive method.

However, my tests in Python yielded different results. Surprisingly, the explicit formula approach was slower than the iterative method. For smaller Fibonacci numbers, the explicit formula performed well, but larger numbers introduced precision loss due to floating-point operations.

### Memoization for Optimization

During my research, I found that **memoization** can significantly speed up recursive functions. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again, avoiding redundant calculations.

In Python, the `@lru_cache` decorator from the [`functools`](https://docs.python.org/3/library/functools.html) module is an easy and efficient way to implement memoization. I used this in the final recursive function to improve performance.

Additionally, I used Python's [`decimal`](https://docs.python.org/3/library/decimal.html) module to control the precision of floating-point calculations when using Binet's formula, in an attempt to reduce information loss during Fibonacci number computations.

### Experiments and Takeaways

In my experiments, I compared various Fibonacci calculation methods, optimizing for both performance and accuracy. Below are the different approaches used, with performance measured using the `timer` decorator:

The [`fibonacci.py](../../fibonacci.py) file includes several functions for calculating Fibonacci numbers:

* [`fibo_recs(n)`](../../fibonacci.py#L12): Recursive implementation (optimized with memoization).
* [`fibo_iter(n)`](../../fibonacci.py#L34): Iterative implementation.
* [`fibo_math(n)`](../../fibonacci.py#L58): Direct calculation using Binet's formula (with the `math` module).
* [`fibo_decm(n)`](../../fibonacci.py#L85): Direct calculation using Binet's formula (with the `decimal` module for higher precision).
* [`fibo_matx(n)`](../../fibonacci.py#L113): Matrix exponentiation approach.

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

While results for recursion without memoization are not included here because its high computational cost limited the number of samples I could test—my laptop struggled with any values of $n >= 50$, notably, the memoized version consistently outperformed all other approaches in every experiment, this can be corroborated with further analysis below.

### Raw observations of average trends and data visualization

For this part, `timer` was adjusted to return a [list](./fibonacci_results_wrapper.json) of the average execution time for 100 runs of each function with increasing `n` from 10 to 250.

This graph displays a compelling visualization of the performance of different Fibonacci number calculation methods as the input size (n) increases. Here's a breakdown of the key observations:

![This is a graph showing the performance of different Fibonacci functions](./fibonacci_results_wrapper_1.png)

#### Overall trends

* **Clear performance differences**: This graph effectively contrast the performance differences between each of the Fibonacci implementations. Some methods exhibit consistent efficiency, while others show noticeable increases in execution time as `n` grows.

* **Memoized Recursion**: Using the `@lru_cache` decorator, the memoized recursive approach (`fibo_recs`) demostrates remarkably consistent and fast performance across the entire range of input values. On the graph, the average execution time curve behaves as nearly a flat line, indicating that the execution times remain constant even as `n` increases, or the differences in performance are neglictible in the scale analyzed (microseconds). This underscores the power of memoization in optimizing recursive algorithms, and hightlights the potential of the iterative approach over the rest of presented solutions.

* **Binet's Explicit Formula**: Binet's formula provides a direct mathematical calculation, which should have a constant time complexity (O(1)). The execution time should ideally not be significantly affected by the input size. The formula implemented with the standard `math` module (`fibo_math`) did not show a gradual increase in execution time, although in each moment, the execution time was higher compared with the memoized recursive function `fibo_recs`. This might be due to the computational cost of exponentiation and floating-point operations involved in the formula. Besides, as the number increased, the outputs progressively started from expected outputs. Only for smaller values of `n` the execution time was slower than the iterative approach `fibo_iter`.

* **Iteration**: The iterative approach (`fibo_iter`) shows a gradual, almost linear increase in execution time as `n` increases. This is expected for an iterative solution where the number of operations directly correlates with the input size. It's intriguing why this behaviour is not observed in a recursive approach, even with the LRU aid.

* **Controlled precision with `Decimal`**: Using the `Decimal` module for higher precision in Binnet's formula (`fibo_decm`) leads to a more pronounced increase in execution time as `n` grows. This hightlights the performance overhead associated with arbitrary-precision arithmetic. More targeted test cases are needed to understand better the impact of adjusting the precision in performance, memory and precision.

* **Matrix Exponentiation**: The matrix exponentiation approach (`fibo_matx`) shows an interesting trend with a relatively steep initial increase in execution time, followed by a more moderate growth. This suggests that the matrix operations might have a higher initial overhead but scale relatively well with larger inputs. For the test ran initially, the matrix exponentiation did not have an impact on precision.

#### Outliers and Variations

* **Outliers**: During several tests, a pyke in the `fibo_matx` was consistenly observed, associated to the `n = 37` or near values. Presumably, this outlier is be due to various factors like the python garbage collection processes, memory allocation, caching behaviour, or other system-level events. It would be interesting to conduct more specific tests to delve into this outlier causes.

* **Variations**: There are minor fluctuations on the execution times for all functions, shared in common for each fuction, but more pronounced in `fibo_matx` and `fibo_decm`. In fact, a sort of cyclic behaviour where the performance time increase and decrease progressively can be observed for both lines in the graph. This can be due to system factors as load, caching effects, and variations in hardware or interpreter performance. Both `fibo_matx` and `fibo_decm` are expected to consume more memory, so it make sense that these two are more affected by the aforementioned factors compared with the remaining approaches.  

---
**Key Takeaways**:

- **Memoization**: The `fibo_recs` function performs much better with memoization, significantly reducing redundant calculations, making it an efficient recursive approach.  

- **Iterative vs. Mathematical**: The iterative approach (`fibo_iter`) generally outperforms the mathematical calculation (`fibo_math`) for large Fibonacci numbers due to reduced overhead.

- **Precision**: For very large Fibonacci numbers, the `decimal` module ensures higher accuracy in calculations but at the cost of increased execution time.

- **Performance vs. Accuracy**: There's a trade-off between performance and accuracy. Using `Decimal` improves precision but increases computation time.

- **Floating-Point Limitations**: Floating-point arithmetic can lead to precision issues when using Binet's formula for very large Fibonacci numbers.