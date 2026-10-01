import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_05 = import_module("05_fibonacci_series")

assert module_05.generate_fibonacci(5) == [0, 1, 1, 2, 3]
assert module_05.generate_fibonacci(1) == [0]
assert module_05.generate_fibonacci(0) == []
assert module_05.generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

print("All test cases passed.")