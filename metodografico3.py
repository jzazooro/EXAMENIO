from scipy.optimize import linprog

print("Apartado a")

# Coeficientes de la función objetivo
c = [-8, -5]  # Se usan valores negativos porque linprog realiza minimización por defecto

# Coeficientes de las restricciones de desigualdad (lado izquierdo)
A = [[2, 1],            # Restricción de plástico
     [3/60, 4/60],      # Restricción de tiempo de producción
     [1, 1],            # Restricción de producción total
     [1, -1]]           # Relación entre Space Rays y Zappers

# Lado derecho de las restricciones de desigualdad
b = [1200,  # kg de plástico
     40,    # horas de producción
     800,   # producción total
     450]   # diferencia máxima entre Space Rays y Zappers

# Resolver el problema de programación lineal
optimal_solution = linprog(c, A_ub=A, b_ub=b, method='highs')

print(optimal_solution.x, -optimal_solution.fun)  # Variables de decisión óptimas y utilidad máxima


import matplotlib.pyplot as plt
import numpy as np

# Definir el rango para las variables x1 (Space Rays) y x2 (Zappers)
x1 = np.linspace(0, 800, 400)  # Rango de valores para x1

# Restricciones
plastico = (1200 - 2*x1) / 1    # 2x1 + 1x2 <= 1200
produccion = (2400 - 3*x1) / 4  # 3x1 + 4x2 <= 2400 (2400 es 40 horas en minutos)
total = 800 - x1                # x1 + x2 <= 800
relacion = 450 + x1             # x1 - x2 <= 450

# Configurar el gráfico
plt.figure(figsize=(10, 8))
plt.xlim(0, 800)
plt.ylim(0, 800)
plt.xlabel('Space Rays (x1)')
plt.ylabel('Zappers (x2)')

# Dibujar las líneas de restricción
plt.plot(x1, plastico, label='2x1 + x2 <= 1200')
plt.plot(x1, produccion, label='3x1 + 4x2 <= 2400')
plt.plot(x1, total, label='x1 + x2 <= 800')
plt.plot(x1, relacion, label='x1 - x2 <= 450')

# Rellenar el área factible
y2 = np.minimum(np.minimum(plastico, produccion), total)
plt.fill_between(x1, 0, y2, where=(x1 <= 800) & (x1 - x1/2 <= 450), color='gray', alpha=0.5)

# Añadir leyenda y título
plt.legend()
plt.title('Área Factible de Producción de Juguetes')

# Mostrar el gráfico
plt.show()


print("Apartado b")
# Cálculo de x1 y Z sin Zappers

# Restricciones aplicables
max_plastico = 1200 / 2  # 2x1 <= 1200
max_produccion = (40 * 60) / 3  # 3x1 <= 2400 minutos (40 horas)
max_total = 800  # x1 <= 800

# El máximo x1 es el mínimo de las restricciones
max_x1 = min(max_plastico, max_produccion, max_total)

# Calcular la utilidad máxima Z
max_Z = 8 * max_x1

print(max_x1, max_Z)

print("Apartado c")
# Cálculo de x2 y Z sin Space Rays

# Restricciones aplicables
max_plastico_zappers = 1200  # 1x2 <= 1200
max_produccion_zappers = (40 * 60) / 4  # 4x2 <= 2400 minutos (40 horas)
max_total_zappers = 800  # x2 <= 800

# El máximo x2 es el mínimo de las restricciones
max_x2 = min(max_plastico_zappers, max_produccion_zappers, max_total_zappers)

# Calcular la utilidad máxima Z
max_Z_zappers = 5 * max_x2

print(max_x2, max_Z_zappers)

print("Apartado d") 
print("Sí, la solución con x1=100 y x2 =150 es factible porque cumple con todas las restricciones del problema inicial.")

print("Apartado e")
print("No, la solución con x1=500 y x2 =150 no es factible porque excede la restricción de plástico disponible.")