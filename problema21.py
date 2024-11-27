
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


x = sp.symbols('x')
f = x**3 - 4*x**2 + 6*x


f_prime = sp.diff(f, x)


x0 = 2
y0 = f.subs(x, x0)
slope = f_prime.subs(x, x0)

x_vals = np.linspace(-1, 4, 100)
y_vals = [f.subs(x, val) for val in x_vals]


def tangent_line(x_val):
    return slope * (x_val - x0) + y0

plt.plot(x_vals, y_vals, label='f(x) = x^3 - 4x^2 + 6x', color='blue')
plt.plot(x_vals, tangent_line(x_vals), label='Tangente en x=2', color='red', linestyle='--')
plt.scatter([x0], [y0], color='green')  # Punto de tangencia
plt.title('Gráfica de la función y su tangente')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
