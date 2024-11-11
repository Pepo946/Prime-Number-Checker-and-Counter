# Prime Number Checker and Counter
 This Python script is designed to check whether a number is prime and count how many prime numbers exist in a given range.

note_content = """
# Prime Number Checker and Counter

## Overview:
This Python script is designed to check whether a number is prime and count how many prime numbers exist in a given range. It includes a function `is_prime(n)` that efficiently checks if a number is prime, optimized by:
- Checking if the number is less than or equal to 1 (not prime).
- Identifying 2 as a prime number directly.
- Skipping even numbers greater than 2.
- Using the square root method to reduce unnecessary checks.

The script counts the prime numbers in the range from 100 to 151 and prints the total count (which is 17 in this case).

## How it Works:
1. **Prime Number Check (`is_prime`)**:
   - If `n <= 1`, return `False` (the number is not prime).
   - If `n == 2`, return `True` (2 is prime).
   - If `n` is even and greater than 2, return `False`.
   - For odd numbers, check divisibility from 3 up to the square root of `n` (inclusive).
   - If no divisors are found, return `True` (the number is prime).

2. **Count Prime Numbers in Range**:
   - The script loops over the numbers from 100 to 151 and applies the `is_prime` function to count how many are prime.

## Example Output:
