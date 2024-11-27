import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 400)
onda1 = np.sin(x)
onda2 = np.cos(x)
superposicion = onda1 + onda2

plt.figure(figsize=(10, 6))
plt.plot(x, onda1, label='Onda 1 (sin(x))')
plt.plot(x, onda2, label='Onda 2 (cos(x))')
plt.plot(x, superposicion, label='Superposición', linestyle='--')
plt.title('Superposición de dos ondas')
plt.xlabel('x')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()
