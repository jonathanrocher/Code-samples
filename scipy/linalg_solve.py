from numpy import *
from scipy.linalg import inv, solve, lu_factor, lu_solve, det, lstsq
from numpy.linalg import cond

A = array([[ 1.        ,  2.67499884,  7.15561882 ],
       [ 1.        ,  2.44819414,  5.99365454],
       [ 1.        ,  2.30846879,  5.32902817]], dtype = float64)
       
print "Near singular matrix if cond is large or det is close to 0", cond(A), det(A)

inverse_matrix = inv(A)
if not allclose(A.dot(inverse_matrix), identity(3)):
    raise ValueError("Matrix inversion in viscosity computation failed.")

Y = array([1e15, 1e3, 1.], dtype = float64)
#Y = array([5, 3, 1.], dtype = float64)

# Manual way
X = dot(inverse_matrix,Y)

# More efficient way: the solver doesn't compute the full inverse, since it is not needed.
X = solve(A,Y)

# LU decomposition actually returns just like solve: it probably implements LU behind the scene.
lu, piv = lu_factor(A)
X = lu_solve((lu, piv), Y)

# The least square solver offers a different algorithm to compute this in order
# to minimize |Y-AX|.
X, residues, rank, singular_values = lstsq(A, Y)

if not allclose(dot(A,X), Y):
    raise ValueError("The solution from the inversion is incorrect: %s"
                      % dot(A,X))