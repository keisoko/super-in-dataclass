"""My python modules"""

import random
import string


def operate(func, item):
    """Executes the higher-order function"""
    return func(item)


def generate_id(length: int):
    """Helper function to generate id."""
    return "".join(random.choices(string.hexdigits.upper(), k=length))
