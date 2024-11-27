import matplotlib.pyplot as plt

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

def fibonacci_acumulativo(n):
    fib_series = fibonacci(n)
    acumulado = [sum(fib_series[:i+1]) for i in range(n)]
    return acumulado

n = 10
indices = list(range(n))
acumulado = fibonacci_acumulativo(n)

plt.bar(indices, acumulado)
plt.xlabel('Índices de Fibonacci')
plt.ylabel('Suma Acumulada')
plt.title('Gráfica de Fibonacci Acumulativo')
plt.show()

