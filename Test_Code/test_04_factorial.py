import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_04 = import_module("04_factorial")

assert module_04.calculate_factorial(5) == 120
assert module_04.calculate_factorial(0) == 1
assert module_04.calculate_factorial(1) == 1
assert module_04.calculate_factorial(6) == 720
assert module_04.calculate_factorial(4) == 24

print("All test cases passed.")