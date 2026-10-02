import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_10 = import_module("10_sum_of_digits")

assert module_10.sum_of_digits(123) == 6
assert module_10.sum_of_digits(0) == 0
assert module_10.sum_of_digits(9) == 9
assert module_10.sum_of_digits(1000) == 1
assert module_10.sum_of_digits(-456) == 15

print("All test cases passed.")