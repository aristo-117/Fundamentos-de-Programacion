import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')
P = x**3 - 6*x**2 + 11*x - 6


raices = sp.solve(P, x)


x_vals = np.linspace(0, 4, 400)
P_vals = [P.subs(x, val) for val in x_vals]


plt.plot(x_vals, P_vals, label='P(x)', color='blue')


for raiz in raices:
    plt.plot(float(raiz), float(P.subs(x, raiz)), 'ro')  # 'ro' para puntos rojos
    plt.annotate(f'Raíz: {raiz}', xy=(float(raiz), float(P.subs(x, raiz))),
                 xytext=(float(raiz), float(P.subs(x, raiz)) + 1),
                 arrowprops=dict(facecolor='black', shrink=0.05))


plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('Gráfica del Polinomio P(x)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.legend()
plt.grid()
plt.show()
