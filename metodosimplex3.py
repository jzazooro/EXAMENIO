from scipy.optimize import linprog

# Costos por kilogramo
costo_azucar = 1.5
costo_gelatina = 2.5

# Coeficientes de la función de costos
c = [costo_azucar, costo_gelatina]  # Costos de azúcar y gelatina respectivamente

# Coeficientes de las restricciones de desigualdad (peso total adaptado y peso total real)
A = [[2, 1],  # Coeficientes para el peso adaptado (azúcar x2, gelatina x1)
     [-1, -1]]  # Coeficientes para el peso real (azúcar x1, gelatina x1)

# Lados derechos de las restricciones de desigualdad
b = [90,  # Peso total adaptado máximo
     -50]  # Peso total real mínimo (negativo porque la restricción es ≥)

# Restricción de igualdad para la cantidad máxima de azúcar
A_eq = [[1, 0]]  # Solo importa la cantidad de azúcar
b_eq = [10]  # Máximo de azúcar permitido

# Límites para las variables (azúcar y gelatina)
# Azúcar debe ser al menos 0 y a lo máximo 10, Gelatina debe ser al menos 0
x0_bounds = (0, 10)
x1_bounds = (0, None)

# Resolver el problema de programación lineal
res = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=[x0_bounds, x1_bounds], method='highs')

print(res.x)  # Cantidades óptimas de azúcar y gelatina

# Costo de producción por pastel
costo_produccion = 10 * costo_azucar + 40 * costo_gelatina

# Precio de venta por pastel
precio_venta = 150

# Margen por pastel
margen = precio_venta - costo_produccion
print(margen)
