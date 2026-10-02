import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_16 = import_module("16_remove_duplicates")

assert module_16.remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert module_16.remove_duplicates([1, 1, 1]) == [1]
assert module_16.remove_duplicates([1, 2, 3]) == [1, 2, 3]

print("All test cases passed.")