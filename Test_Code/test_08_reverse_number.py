import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_08 = import_module("08_reverse_number")

assert module_08.reverse_number(123) == 321
assert module_08.reverse_number(1000) == 1
assert module_08.reverse_number(0) == 0
assert module_08.reverse_number(-456) == -654
assert module_08.reverse_number(7) == 7

print("All test cases passed.")