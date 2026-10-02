import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_13 = import_module("13_palindrome_string")

assert module_13.is_palindrome_string("madam") == True
assert module_13.is_palindrome_string("hello") == False
assert module_13.is_palindrome_string("Madam") == True
assert module_13.is_palindrome_string("a") == True

print("All test cases passed.")