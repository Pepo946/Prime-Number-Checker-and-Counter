# Prime Number Checker and Counter 🚀

## 🧐 Overview:
This Python script is your go-to tool for checking whether numbers are prime and counting how many prime numbers exist in a specific range. With optimized methods for performance, it's both efficient and fun to work with!

The `is_prime(n)` function has a few tricks up its sleeve:
- 🚫 It immediately returns `False` for numbers less than or equal to 1 (because those aren’t prime).
- ✔️ It gives a big thumbs up for the number 2 (the smallest prime number).
- 🧮 It skips even numbers greater than 2, saving time by not testing numbers like 4, 6, 8, and so on.
- 🔍 It uses the square root method to reduce unnecessary checks, making it much faster than checking every number up to `n`.

In this script, we’re focusing on counting prime numbers within the range of 100 to 151. And guess what? The total number of primes in that range is **17**!

## ⚙️ How It Works:
1. **Prime Number Check (`is_prime`)**:
   - First, if the number is less than or equal to 1, it’s an automatic **No** (return `False`).
   - If it’s exactly **2**, it gets a prime stamp (return `True`).
   - If the number is even and greater than 2, we know it's **not** prime (return `False`).
   - For odd numbers, we check divisibility by odd numbers starting from 3 up to the square root of the number. This significantly reduces the checks needed.
   - If no divisors are found, **it’s prime**! (return `True`).

2. **Counting Primes**:
   - The script checks every number in the range from 100 to 151 and applies the `is_prime` function to count how many are prime.

## 🖥️ Example Output:
When you run the script, you’ll get something like this:

```bash
Prime numbers between 100 and 151: [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
The total number of primes: 17
