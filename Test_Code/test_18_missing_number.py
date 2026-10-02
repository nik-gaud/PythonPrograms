import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_18 = import_module("18_missing_number")

assert module_18.find_missing_number([1, 2, 4, 5], 5) == 3
assert module_18.find_missing_number([1, 2, 3, 4], 5) == 5
assert module_18.find_missing_number([2, 3, 4, 5], 5) == 1

print("All test cases passed.")