"""
bug_pool.py — the pool of seedable defects.

Each entry is ONE realistic, small bug targeting exactly one function.
`find` must appear exactly once in the target file (seed_bugs.py checks this).
`category` ties each bug back to a course concept, for instructor reporting.

IMPORTANT: this file (and the reference implementations) are the instructor's
answer key. Do not share this file with students.
"""

BUG_POOL = [
    {
        "id": "BUG-01",
        "file": "business_utils.py",
        "function": "is_eligible_for_membership",
        "category": "boundary (off-by-one)",
        "description": "Uses > instead of >= — an 18-year-old is wrongly rejected.",
        "find": "    return age >= 18",
        "replace": "    return age > 18",
    },
    {
        "id": "BUG-02",
        "file": "business_utils.py",
        "function": "calculate_late_fee",
        "category": "wrong constant",
        "description": "Late fee rate is 0.5, mutated to 0.05 (10x too cheap).",
        "find": "    return days_late * 0.5",
        "replace": "    return days_late * 0.05",
    },
    {
        "id": "BUG-03",
        "file": "business_utils.py",
        "function": "apply_discount",
        "category": "wrong operator",
        "description": "Multiplies by 1.1 instead of 0.9 — members get overcharged.",
        "find": "        return price * 0.9",
        "replace": "        return price * 1.1",
    },
    {
        "id": "BUG-04",
        "file": "business_utils.py",
        "function": "calculate_shipping_cost",
        "category": "boundary (off-by-one)",
        "description": "Uses < instead of <= — exactly 1kg is charged the higher rate.",
        "find": "    if weight <= 1:",
        "replace": "    if weight < 1:",
    },
    {
        "id": "BUG-05",
        "file": "text_utils.py",
        "function": "is_valid_password",
        "category": "boundary (off-by-one)",
        "description": "Uses >= 8 mutated to > 8 — an 8-character password is wrongly rejected.",
        "find": "    return len(password) >= 8",
        "replace": "    return len(password) > 8",
    },
    {
        "id": "BUG-06",
        "file": "text_utils.py",
        "function": "truncate_text",
        "category": "boundary (off-by-one)",
        "description": "Uses > instead of >= — text exactly max_len long is truncated unnecessarily.",
        "find": "    if len(text) > max_len:",
        "replace": "    if len(text) >= max_len:",
    },
    {
        "id": "BUG-07",
        "file": "text_utils.py",
        "function": "is_palindrome",
        "category": "missing normalization",
        "description": "Forgets to lowercase — \"Racecar\" is wrongly reported as not a palindrome.",
        "find": "    normalized = text.lower()",
        "replace": "    normalized = text",
    },
    {
        "id": "BUG-08",
        "file": "text_utils.py",
        "function": "count_vowels",
        "category": "incomplete condition",
        "description": "Only counts lowercase vowels — uppercase vowels are missed.",
        "find": '    vowels = set("aeiouAEIOU")',
        "replace": '    vowels = set("aeiou")',
    },
    {
        "id": "BUG-09",
        "file": "text_utils.py",
        "function": "reverse_words",
        "category": "wrong logic",
        "description": "Reverses each word's letters instead of reversing word order.",
        "find": '    return " ".join(sentence.split()[::-1])',
        "replace": '    return " ".join(w[::-1] for w in sentence.split())',
    },
    {
        "id": "BUG-10",
        "file": "math_utils.py",
        "function": "calculate_average",
        "category": "wrong operator",
        "description": "Uses integer division // instead of / — average is truncated.",
        "find": "    return sum(numbers) / len(numbers)",
        "replace": "    return sum(numbers) // len(numbers)",
    },
    {
        "id": "BUG-11",
        "file": "math_utils.py",
        "function": "find_max",
        "category": "wrong initialization",
        "description": "Starts from numbers[0] mutated to start from 0 — fails for all-negative lists.",
        "find": "    largest = numbers[0]",
        "replace": "    largest = 0",
    },
    {
        "id": "BUG-12",
        "file": "math_utils.py",
        "function": "is_prime",
        "category": "boundary (off-by-one)",
        "description": "Boundary check n < 2 mutated to n < 1 — is_prime(1) wrongly returns True.",
        "find": "    if n < 2:",
        "replace": "    if n < 1:",
    },
    {
        "id": "BUG-13",
        "file": "math_utils.py",
        "function": "is_leap_year",
        "category": "missing case",
        "description": "Drops the %400 exception — century years like 2000 are wrongly excluded.",
        "find": "    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)",
        "replace": "    return year % 4 == 0 and year % 100 != 0",
    },
    {
        "id": "BUG-14",
        "file": "math_utils.py",
        "function": "calculate_bmi",
        "category": "wrong formula",
        "description": "Forgets to square height — formula becomes weight / height.",
        "find": "    return weight_kg / (height_m ** 2)",
        "replace": "    return weight_kg / height_m",
    },
]
