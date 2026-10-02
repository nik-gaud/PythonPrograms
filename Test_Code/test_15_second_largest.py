import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_15 = import_module("15_second_largest")

assert module_15.second_largest([10, 20, 4, 45, 99]) == 45
assert module_15.second_largest([1, 2, 3]) == 2
assert module_15.second_largest([5, 5, 4]) == 4

print("All test cases passed.")