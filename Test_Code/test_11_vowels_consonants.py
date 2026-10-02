import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_11 = import_module("11_vowels_consonants")

assert module_11.count_vowels_consonants("Hello") == (2, 3)
assert module_11.count_vowels_consonants("Python") == (1, 5)
assert module_11.count_vowels_consonants("AEIOU") == (5, 0)
assert module_11.count_vowels_consonants("xyz") == (0, 3)

print("All test cases passed.")