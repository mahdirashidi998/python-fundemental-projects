from sympy.solvers import solve
from sympy import Symbol
x=Symbol('x')
print(solve(x*(x+0.065),x))
