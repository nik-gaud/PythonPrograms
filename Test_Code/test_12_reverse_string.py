import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_12 = import_module("12_reverse_string")

assert module_12.reverse_string("hello") == "olleh"
assert module_12.reverse_string("Python") == "nohtyP"
assert module_12.reverse_string("a") == "a"
assert module_12.reverse_string("") == ""

print("All test cases passed.")