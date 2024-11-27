from sympy import symbols, diff
from sympy import pprint

def derivada_diferencias_finitas(funcion, x_valor, h=1e-5):
    x = symbols('x')
    derivada = (funcion.subs(x, x_valor + h) - funcion.subs(x, x_valor - h)) / (2 * h)
    return derivada

x = symbols("x")
funcion = 3*x**2 + 2*x
punto = 1  # Punto en el que se desea calcular la derivada

resultado = derivada_diferencias_finitas(funcion, punto)
print("Resultado: ")
pprint(resultado)
