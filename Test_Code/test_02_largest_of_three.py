import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_02 = import_module("02_largest_of_three")

assert module_02.find_largest(10, 5, 3) == 10
assert module_02.find_largest(2, 8, 6) == 8
assert module_02.find_largest(1, 4, 9) == 9
assert module_02.find_largest(5, 5, 3) == 5
assert module_02.find_largest(-1, -5, -3) == -1

print("All test cases passed.")