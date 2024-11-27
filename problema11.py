import sympy as sp
x = sp.symbols('x')
def tangente_a_curva(funcion, punto):
    f = funcion(x)
    derivada = sp.diff(f, x)
    pendiente = derivada.subs(x, punto)
    intercepto = f.subs(x, punto) - pendiente * punto #Calcula el intercepto en el eje y de la recta tangente usando la fórmula
    return pendiente, intercepto

funcion = lambda x: x**2 + 2*x + 1 #Define la función
punto = 1
pendiente, intercepto = tangente_a_curva(funcion, punto)
print(f"Ecuación de la recta tangente: y = {pendiente}x + {intercepto}")
