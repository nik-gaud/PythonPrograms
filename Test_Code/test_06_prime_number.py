import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_06 = import_module("06_prime_number")

assert module_06.check_prime(7) == True
assert module_06.check_prime(10) == False
assert module_06.check_prime(2) == True
assert module_06.check_prime(1) == False
assert module_06.check_prime(17) == True

print("All test cases passed.")
