import sympy as sp

def resolver_sistema(ecuaciones):
    return sp.linsolve(ecuaciones, (x, y, z))

x, y, z = sp.symbols('x y z')

ecuacion1 = sp.Eq(2*x - y + z, 5)
ecuacion2 = sp.Eq(3*x + 2*y - 4*z, 3)
ecuacion3 = sp.Eq(x + y + z, 6)

sistema = [ecuacion1, ecuacion2, ecuacion3]
solucion = resolver_sistema(sistema)

print(solucion)
