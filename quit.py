from sympy.abc import x, y, z, a, b
from sympy import solve, Poly, Eq, Function, exp

f = Function('f')
solve(x < 3)
sol = solve(x - 3, dict = True)
sol
solutionTwo = solve([x - 3, y - 1], dict = True)
solutionTwo
solutionTwo[0][x]
solutionTwo[0][y]
