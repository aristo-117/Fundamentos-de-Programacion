def suma_fibonacci(n):
    a, b = 0, 1
    suma = 0
    for _ in range(n):
        suma += a
        a, b = b, a + b
    return suma


n = int(input("Ingrese el número de términos: "))
resultado = suma_fibonacci(n)
print(f"La suma de los primeros {n} términos de la serie de Fibonacci es: {resultado}")