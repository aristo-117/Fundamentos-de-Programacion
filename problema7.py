from sympy import symbols, diff
from sympy import pprint
x=symbols("x")
funcion = 3*x**2 + 2*x

funcion_derivada =diff(funcion, x)
print("Resultado: ")
pprint(funcion_derivada)
