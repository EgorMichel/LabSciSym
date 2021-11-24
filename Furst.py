import numpy as np
import sympy

r, l, n = sympy.symbols('r l n')
A = sympy.Matrix(np.zeros((9, 9)))
A[0, 3] = -1 / r
A[1, 4] = -1 / r
A[2, 5] = -1 / r
A[3, 0] = -(l + 2 * n)
A[4, 1] = -n
A[5, 2] = -n
A[6, 0] = -l
A[8, 0] = -l

sympy.pprint(A.eigenvals())
