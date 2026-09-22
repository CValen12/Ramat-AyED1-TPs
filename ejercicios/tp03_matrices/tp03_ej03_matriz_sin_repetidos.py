"""
3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N²), de tal forma que ningún número se repita.
Al imprimir la matriz por pantalla.
"""
import random

def _matriz(n: int) -> list[list[int]]:
    """
    Rellena una matriz de N x N con enteros al azar sin repetirse.

    Pre: Recibe un entero positivo mayor a cero.

    Post: Retorna una matriz (lista de listas de enteros).
    """
    assert n > 0, "El valor de n debe ser un entero positivo."
    
    matriz_resultado = []
    limite = n ** 2
    usados = []
    
    for fila in range(n):
        fila_actual = []
        while len(fila_actual) < n:
            numero = random.randint(0, limite)
            if numero not in usados:
                usados.append(numero)
                fila_actual.append(numero)
                
        matriz_resultado.append(fila_actual)
    return matriz_resultado


def main() -> None:        
    n = int(input("Ingrese el valor de n para la matriz n x n: "))
    
    matriz_norepetidos = _matriz(n)
        
    print("\nMatriz:")
    for fila in matriz_norepetidos:
        print(fila)
    
if __name__ == "__main__":
    main()               