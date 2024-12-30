from math import sqrt

def fibo_rec(number: int) -> int | None:
    if isinstance(number, int) and number > 0:
        return number if number in (0,1) else \
        fibo_rec(number - 1) + fibo_rec(number - 2)
    else: 
        raise ValueError("Input must be a positive integer")
        return None
    
def fibo_math(number: int) -> int:
    if isinstance(number, int) and number > 0:
        c = 1 / sqrt(5)
        phi = (1 + sqrt(5))/2
        psi = (1 - sqrt(5))/2

        return round(c * (phi ** number) - (psi ** number))
    else: 
        raise ValueError("Input must be a positive integer")
    
    
if __name__ == "__main__":
    rec_fibo10 = fibo_rec(10)
    print(rec_fibo10)
    mat_fibo10 = fibo_math(10)
    print(mat_fibo10)