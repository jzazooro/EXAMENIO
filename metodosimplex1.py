from pulp import LpMaximize, LpProblem, LpVariable

# Problema de Simplex
"""Max Z = 4 x1 + 5 x2
S.a.:
2 x1 + x2 <= 8
x2 <= 5"""

# Crear el modelo
model = LpProblem(name="small-problem", sense=LpMaximize)

# Definir las variables
x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)

# Añadir las restricciones
model += (2 * x1 + x2 <= 8, "constraint_1")
model += (x2 <= 5, "constraint_2")

# Definir la función objetivo
model += 4 * x1 + 5 * x2

# Resolver el problema
model.solve()

# Obtener y mostrar los resultados
x1_value = x1.value()
x2_value = x2.value()
max_Z = model.objective.value()

print(f"Resultado:\nx1 = {x1_value}\nx2 = {x2_value}\nMax Z = {max_Z}")