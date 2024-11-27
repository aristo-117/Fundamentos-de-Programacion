def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def primo_fibonacci_mas_cercano(n):
    fib = fibonacci(n)
    while not primo(fib):
        n += 1
        fib = fibonacci(n)
    return fib

indice = int(input("Escriba el indeice: "))
resultado = primo_fibonacci_mas_cercano(indice)
print(f"El número primo más cercano en la serie de Fibonacci al índice {indice} es: {resultado}")
