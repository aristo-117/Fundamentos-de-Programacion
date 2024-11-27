def calcular_factorial(n):
    if n < 0:
        return "Numero invalido."
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

n = int(input("Ingrese un número entero N: "))
resultado = calcular_factorial(n)
print(f"El factorial de {n} es: {resultado}")