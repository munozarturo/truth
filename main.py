from typing import Callable
from truth import truth_table, pretty_print

f:  Callable = lambda a, b, c_in: a ^ b ^ c_in
f1: Callable = lambda a, b: a ^ b

f_table = truth_table(f)
pretty_print(f_table, columns=["#", "a", "b", "c_in", "f(x)"], title="F", rep_true="1", rep_false="0")

f1_table = truth_table(f1)
pretty_print(f1_table, columns=["#", "a", "b", "a ^ b"], title="F1", rep_true="1", rep_false="0")