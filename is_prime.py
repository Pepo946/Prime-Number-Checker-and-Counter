import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

# عد الأعداد الأولية في النطاق من 100 إلى 151
count = 0
for n in range(100, 152):
    if is_prime(n):
        count += 1

print(count)  # النتيجة ستكون 17
