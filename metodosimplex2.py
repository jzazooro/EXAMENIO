from scipy.optimize import linprog

# Problema de Simplex
"""Max Z = 6 x1 + 3 x2
S. a.:
2 x1 + 4 x2 <= 8
- x1 + 4 x2 <= 4
x1 - x2 <= 2
x1; x2 >= 0"""

# Coefficients of the objective function
c = [-6, -3]  # Coefficients are negated for minimization

# Coefficients of the inequality constraints
A = [[2, 4], [-1, 4], [1, -1]]

# Right-hand side of the inequality constraints
b = [8, 4, 2]

# Bounds for each variable
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# Solving the linear programming problem using the Simplex method
res_simplex = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

print(res_simplex.x, -res_simplex.fun)  # Solution and maximum value of the objective function