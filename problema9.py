from sympy import symbols, diff, solve
from sympy import pprint

x = symbols("x")
funcion = 3*x**2 + 2*x

funcion_derivada = diff(funcion, x)
pprint(funcion_derivada)

#mínimo o máximo
puntos_criticos = solve(funcion_derivada, x)
pprint(puntos_criticos)

#Calcular la segunda derivada
segunda_derivada = diff(funcion_derivada, x)
pprint(segunda_derivada)

#Evaluar puntos críticos
for punto in puntos_criticos:
    evaluacion = segunda_derivada.subs(x, punto)
    pprint(f"Evaluación en {punto}: {evaluacion}")
