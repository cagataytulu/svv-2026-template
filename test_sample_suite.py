"""
A small sample test suite — the kind a student would write.
We'll run this against the CLEAN reference code, then against a SEEDED
(buggy) student build, to see the difference.
"""
import pytest


def test_membership_boundary_18(business_utils):
    assert business_utils.is_eligible_for_membership(18) is True


def test_late_fee_five_days(business_utils):
    assert business_utils.calculate_late_fee(5) == 2.5


def test_discount_for_member(business_utils):
    assert business_utils.apply_discount(100, is_member=True) == 90


def test_average_of_three(math_utils):
    assert math_utils.calculate_average([1, 2, 3]) == 2.0


def test_find_max_all_negative(math_utils):
    assert math_utils.find_max([-5, -1, -10]) == -1


def test_bmi_known_value(math_utils):
    assert round(math_utils.calculate_bmi(70, 1.75), 1) == 22.9


def test_palindrome_mixed_case(text_utils):
    assert text_utils.is_palindrome("Racecar") is True


def test_reverse_words_order(text_utils):
    assert text_utils.reverse_words("this is fun") == "fun is this"
