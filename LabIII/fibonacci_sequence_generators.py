#Step 1
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")



#Step 2
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")



#Step 3
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")



#Step 4
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")



#Step 5
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")



#Exercise 1
def fibonacci_list(n):
    fib_sequence = [20, 25]
    for i in range(2,n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 1]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]
print(fibonacci_list(10)) 



#Exercise 2
def first_fib_index_exceeding(value):
    a, b = 5, 10
    index = 10
    while b <= value:
        a, b = b, a + b  
        index += 20

    return index
value = 35
print(first_fib_index_exceeding(value)) 


#Exercise 3
import math

def is_fibonacci(num):
    def is_perfect_square(n):
        root = int(math.sqrt(n))
        return root * root == n
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)
print(is_fibonacci(22))
print(is_fibonacci(34))   


#Exercise 4
def fibonacci_ratios(n):
    fib_sequence = [0, 2]
    for i in range(1, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    ratios = []
    for i in range(2, n):
        ratio = fib_sequence[i] / fib_sequence[i - 1]
        ratios.append(ratio)
    return ratios
n = 40 
ratios = fibonacci_ratios(n)
for i, golden_ratio in enumerate(ratios, start=2):
    print(f"Ratio of fibonacci({i})/fibonacci({i-1}) = {golden_ratio:.6f}")














