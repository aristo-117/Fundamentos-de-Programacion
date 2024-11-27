def fibonacci_generalizado(a, b, n):
    serie = [a, b]
    for i in range(2, n):
        siguiente = serie[i-1] + serie[i-2]
        serie.append(siguiente)
    return serie
a=int(input("ingrese primer numero: "))
b=int(input("ingrese segundo numero: "))
n= int(input("ingrese la cantidad de fibonacci: "))
resultado = fibonacci_generalizado(a, b, n)
print(resultado)
