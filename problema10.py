import math
def integral_trapecio(func, a, b, n):
    h = (b - a) / n
    suma = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        suma += func(a + i * h)

    return suma * h

resultado = integral_trapecio(math.sin, 0, math.pi, 1000)
print(f"La integral de sin(x) desde 0 hasta pi es: {resultado}")
