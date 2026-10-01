import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_09 = import_module("09_palindrome_number")

assert module_09.is_palindrome_number(121) == True
assert module_09.is_palindrome_number(123) == False
assert module_09.is_palindrome_number(1) == True
assert module_09.is_palindrome_number(1221) == True
assert module_09.is_palindrome_number(-121) == True

print("All test cases passed.")