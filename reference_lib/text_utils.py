"""
text_utils.py — small text-processing functions used across the course examples.
This is the CLEAN, correct reference implementation.
"""


def is_valid_password(password):
    """Spec: a password is valid if it has 8 or more characters."""
    return len(password) >= 8


def truncate_text(text, max_len):
    """Spec: if text is longer than max_len, cut it to max_len chars and add '...'."""
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text


def is_palindrome(text):
    """Spec: True if text reads the same forwards and backwards, ignoring case."""
    normalized = text.lower()
    return normalized == normalized[::-1]


def count_vowels(text):
    """Spec: count how many vowels (a, e, i, o, u) appear, case-insensitive."""
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)


def reverse_words(sentence):
    """Spec: reverse the ORDER of words in a sentence (not the letters)."""
    return " ".join(sentence.split()[::-1])
