import sympy as sp

def obtener_autovalores_y_autovectores(matriz):
    autovalores = matriz.eigenvals()
    autovectores = matriz.eigenvects()
    return autovalores, autovectores

def imprimir_autovalores(autovalores):
    print("Autovalores de la matriz:")
    for valor, multiplicidad in autovalores.items():
        print(f"{valor} con multiplicidad {multiplicidad}")

def imprimir_autovectores(autovectores):
    print("\nAutovectores de la matriz:")
    for valor, multiplicidad, vectores in autovectores:
        print(f"Autovalor: {valor}")
        for vector in vectores:
            print(f"Autovector: {vector}")

M = sp.Matrix([[4, 2], [1, 3]])
autovalores, autovectores = obtener_autovalores_y_autovectores(M)
imprimir_autovalores(autovalores)
imprimir_autovectores(autovectores)
