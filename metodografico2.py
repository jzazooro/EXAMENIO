import numpy as np
import matplotlib.pyplot as plt

# Problema de Programación lineal
"""Max Z = 6 x1 + 3 x2
S. a.:
2 x1 + 4 x2 <= 8
- x1 + 4 x2 <= 4
x1 - x2 <= 2
x1; x2 >= 0"""

# Definición de las restricciones
x = np.linspace(0, 10, 400)
constraint1 = (8 - 2*x) / 4  # 2x1 + 4x2 <= 8
constraint2 = (4 + x) / 4    # -x1 + 4x2 <= 4
constraint3 = x - 2          # x1 - x2 <= 2

# Coeficientes de la función objetivo
c = [6, 3]

# Gráfica de las restricciones
plt.figure(figsize=(10,8))
plt.plot(x, constraint1, label=r'$2x_1 + 4x_2 \leq 8$')
plt.plot(x, constraint2, label=r'$-x_1 + 4x_2 \leq 4$')
plt.plot(x, constraint3, label=r'$x_1 - x_2 \leq 2$')

# Relleno de la región factible
y = np.minimum(np.minimum(constraint1, constraint2), constraint3)
plt.fill_between(x, np.maximum(0, y), y, where=(y>0), color='gray', alpha=0.3)

# Etiquetas y límites
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Líneas adicionales
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)

# Leyenda
plt.legend()

# Mostrar gráfico
plt.show()

import numpy as np
from scipy.optimize import linprog

# Coeficientes de las restricciones de desigualdad (lado izquierdo)
A = [[2, 4], [-1, 4], [1, -1]]

# Coeficientes de las restricciones de desigualdad (lado derecho)
b = [8, 4, 2]

# Límites para cada variable (x1 y x2)
x0_bounds = (0, None)
x1_bounds = (0, None)

# Resolviendo el problema de programación lineal
res = linprog([-6, -3], A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Punto óptimo y valor de la función objetivo
optimal_point = res.x
optimal_value = -res.fun  # Cambiamos el signo de nuevo

print(f"Punto óptimo: {optimal_point}")
print(f"Valor máximo de la función objetivo: {optimal_value}")

print("Es solucion unica")