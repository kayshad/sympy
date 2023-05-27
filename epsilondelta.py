%matplotlib widget
from sympy import *
from sympy_utils import Constant
init_printing(use_latex=True)

epsilon = Constant(0.0001, "epsilon", r"\epsilon", u"\N{Greek Small Letter Epsilon}")
epsilon, epsilon.evalf()

x = symbols("x")
expr = 2 * x
expr


rs = Lt(Abs(x - (5)), epsilon)
s1 = solve(rs, x)
s2 = solveset(rs, x, domain=S.Reals)
rs, s1, s2
