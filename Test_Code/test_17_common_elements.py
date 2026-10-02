import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_17 = import_module("17_common_elements")

assert module_17.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert module_17.common_elements([1, 2], [3, 4]) == []
assert module_17.common_elements([1, 1, 2], [1, 2]) == [1, 2]

print("All test cases passed.")