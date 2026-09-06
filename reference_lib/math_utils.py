"""
math_utils.py — small math functions used across the course examples.
This is the CLEAN, correct reference implementation.
"""


def calculate_average(numbers):
    """Spec: return the arithmetic mean of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """Spec: return the largest number in a non-empty list (may include negatives)."""
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest


def is_prime(n):
    """Spec: True if n is a prime number (n >= 2)."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_leap_year(year):
    """Spec: divisible by 4, except centuries, unless also divisible by 400."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_bmi(weight_kg, height_m):
    """Spec: BMI = weight (kg) / height (m) squared."""
    return weight_kg / (height_m ** 2)
