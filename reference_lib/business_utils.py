"""
business_utils.py — small business-logic functions used across the course examples.
This is the CLEAN, correct reference implementation.
"""


def is_eligible_for_membership(age):
    """Spec: a person is eligible for membership if they are 18 or older."""
    return age >= 18


def calculate_late_fee(days_late):
    """Spec: late fee is $0.50 per day late. Never negative."""
    if days_late <= 0:
        return 0.0
    return days_late * 0.5


def apply_discount(price, is_member):
    """Spec: members get a 10% discount; non-members pay full price."""
    if is_member:
        return price * 0.9
    return price


def calculate_shipping_cost(weight):
    """Spec: $5 flat fee for up to and including 1kg, plus $2 per kg after that."""
    if weight <= 1:
        return 5.0
    return 5.0 + (weight - 1) * 2.0
