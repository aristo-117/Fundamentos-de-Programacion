def posicion_fibonacci(num):
    a, b = 0, 1
    posicion = 0
    while a < num:
        a, b = b, a + b
        posicion += 1
    return posicion if a == num else -1

numero = int(input("Ingrese un número: "))
resultado = posicion_fibonacci(numero)
if resultado != -1:
    print(f"El número {numero} pertenece a la serie de Fibonacci y su posición es {resultado}.")
else:
    print(f"El número {numero} no pertenece a la serie de Fibonacci.")
