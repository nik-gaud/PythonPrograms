import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_03 = import_module("03_pos_neg_zero")

assert module_03.check_pos_neg_zero(5) == "Positive"
assert module_03.check_pos_neg_zero(-5) == "Negative"
assert module_03.check_pos_neg_zero(0) == "Zero"
assert module_03.check_pos_neg_zero(100) == "Positive"
assert module_03.check_pos_neg_zero(-100) == "Negative"

print("All test cases passed.")