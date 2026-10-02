import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Code'))
from importlib import import_module
module_20 = import_module("20_word_frequency")

assert module_20.word_frequency("the cat sat on the mat") == {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
assert module_20.word_frequency("hello hello") == {'hello': 2}
assert module_20.word_frequency("a b c") == {'a': 1, 'b': 1, 'c': 1}

print("All test cases passed.")