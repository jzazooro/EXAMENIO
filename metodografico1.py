import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Problema de Programación lineal
"""Max Z = 4 x1 + 5 x2
S.a.:
2 x1 + x2 <= 8
x2 <= 5"""

# Definición de las restricciones
x = np.linspace(0, 10, 400)
constraint1 = (8 - 2*x)  # 2x1 + x2 <= 8
constraint2 = np.full_like(x, 5)  # x2 <= 5

# Coeficientes de la función objetivo
c = [-4, -5]  # Cambiamos los signos porque linprog busca minimizar

# Coeficientes de las restricciones de desigualdad (lado izquierdo)
A = [[2, 1], [0, 1]]

# Coeficientes de las restricciones de desigualdad (lado derecho)
b = [8, 5]

# Límites para cada variable (x1 y x2)
x0_bounds = (0, None)
x1_bounds = (0, None)

# Resolviendo el problema de programación lineal
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Punto óptimo y valor de la función objetivo
optimal_point = res.x
optimal_value = -res.fun  # Cambiamos el signo de nuevo

# Gráfica con el punto óptimo
plt.figure(figsize=(10,8))
plt.plot(x, constraint1, label=r'$2x_1 + x_2 \leq 8$')
plt.fill_between(x, 0, constraint1, alpha=0.1, color='blue')
plt.plot(x, constraint2, label=r'$x_2 \leq 5$')
plt.fill_betweenx(x, 0, constraint2, alpha=0.1, color='orange')

# Punto óptimo
plt.plot(optimal_point[0], optimal_point[1], 'ro')  # punto rojo
plt.text(optimal_point[0], optimal_point[1], f'  ({optimal_point[0]:.2f}, {optimal_point[1]:.2f})')

# Etiquetas y límites
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Líneas adicionales
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)

# Leyenda
plt.legend()

# Mostrar gráfico
plt.show()

# Imprimir punto óptimo y valor máximo
print(f"Punto óptimo: {optimal_point}")
print(f"Valor máximo de la función objetivo: {optimal_value}")