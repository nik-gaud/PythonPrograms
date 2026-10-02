import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_14 = import_module("14_char_frequency")

assert module_14.char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert module_14.char_frequency("aab") == {'a': 2, 'b': 1}
assert module_14.char_frequency("") == {}

print("All test cases passed.")