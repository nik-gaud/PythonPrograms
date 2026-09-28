import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_01 = import_module("01_even_odd")

assert module_01.check_even_odd(4) == "Even"
assert module_01.check_even_odd(7) == "Odd"
assert module_01.check_even_odd(0) == "Even"
assert module_01.check_even_odd(-3) == "Odd"

print("All test cases passed.")