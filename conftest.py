"""
conftest.py — lets the SAME test file run against either the clean reference_lib
or a seeded student_build, controlled by the TARGET_LIB env var.

Usage:
    TARGET_LIB=reference_lib pytest test_sample_suite.py
    TARGET_LIB=student_build/20210401234 pytest test_sample_suite.py
"""
import importlib
import os
import sys
from pathlib import Path

import pytest

TARGET = os.environ.get("TARGET_LIB", "reference_lib")
TARGET_PATH = Path(__file__).parent / TARGET
sys.path.insert(0, str(TARGET_PATH))


def _load(module_name):
    # Ensure a fresh import each time (module names collide across targets)
    for mod in list(sys.modules):
        if mod == module_name:
            del sys.modules[mod]
    return importlib.import_module(module_name)


@pytest.fixture
def business_utils():
    return _load("business_utils")


@pytest.fixture
def math_utils():
    return _load("math_utils")


@pytest.fixture
def text_utils():
    return _load("text_utils")
