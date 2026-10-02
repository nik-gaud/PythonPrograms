import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_19 = import_module("19_find_duplicates")

assert module_19.find_duplicates([1, 2, 2, 3, 3, 3]) == [2, 3]
assert module_19.find_duplicates([1, 2, 3]) == []
assert module_19.find_duplicates([5, 5, 5]) == [5]

print("All test cases passed.")