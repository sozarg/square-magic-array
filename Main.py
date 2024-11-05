def calcular_constante_magica(n: int) -> int:
    return n * (n**2 + 1) // 2

def tipo_matriz() -> None:
    while True: 
        filas = int(input("¿Cuántas filas tendrá el cuadrado mágico?: "))
        columnas = int(input("¿Cuántas columnas tendrá el cuadrado mágico?: "))
        if filas == columnas:
            print(f"El cuadrado será una matriz de {filas}x{columnas}")
            return filas, columnas
        else:
            print(f"Error, no es matriz cuadrada (mismo numero de filas y columnas). Intente de nuevo")

def cargar_matriz(filas: int, columnas: int) -> list:
    matriz_cuadrado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = int(input(f"Ingrese el número para la fila {i + 1}, columna {j + 1}: "))
            fila += [numero] 
        matriz_cuadrado += [fila]  

    return matriz_cuadrado

def es_cuadrado_magico(matriz: list) -> bool:
    n = len(matriz) 
    constante_magica = calcular_constante_magica(n)
    # M = n*(n2 + 1)/2

    for fila in matriz:
        suma_fila = 0
        for numero in fila:
            suma_fila += numero
        if suma_fila != constante_magica:
            return False

    for j in range(n):
        suma_columna = 0
        for i in range(n):
            suma_columna += matriz[i][j] 
        if suma_columna != constante_magica:
            return False

    suma_diagonal_principal = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i] 
    if suma_diagonal_principal != constante_magica:
        return False

    suma_diagonal_secundaria = 0
    for i in range(n):
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    if suma_diagonal_secundaria != constante_magica:
        return False

    return True

def main():
    filas, columnas = tipo_matriz()
    matriz = cargar_matriz(filas, columnas)  
    if es_cuadrado_magico(matriz):
        print("¡Es un cuadrado mágico!")
    else:
        print("No es un cuadrado mágico.")

main()
