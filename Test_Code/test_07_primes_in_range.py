import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_07 = import_module("07_primes_in_range")

assert module_07.primes_in_range(1, 10) == [2, 3, 5, 7]
assert module_07.primes_in_range(10, 20) == [11, 13, 17, 19]
assert module_07.primes_in_range(1, 1) == []
assert module_07.primes_in_range(2, 2) == [2]

print("All test cases passed.")