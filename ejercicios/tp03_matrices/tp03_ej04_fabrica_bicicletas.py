"""
4. Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa
el día de la semana y cada fila a una de sus fábricas. Ejemplo:

                    (Lunes) (Martes) (Miércoles) (Jueves) (Viernes) (Sábado)
(Fábrica 1)    0       23       150       20       120       25       150
(Fábrica 2)    1       40        75       80         0       80        35
(Fábrica 3)    2       ...       ...      ...       ...      ...       ...
(Fábrica 4)    3       80        80       80        80       80        80

Se solicita:

a. Crear una matriz con datos generados al azar para N fábricas durante una semana,
considerando que la capacidad máxima de fabricación es de 150 unidades por día y
puede suceder que en ciertos días no se fabrique ninguna.

b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.

c. ¿Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica)?

d. ¿Cuál es el día más productivo, considerando todas las fábricas combinadas?

e. Crear una lista por comprensión que contenga la menor cantidad fabricada por cada
fábrica.
"""

import random

def _imprimir_menores(menores: list[int]) -> None:
    """ 
    Imprime por pantalla el menor dia de producción de cada fabrica.
    
    Pre: Recibe una lista de enteros.
    
    Post: Imprime el resultado
    """
    print(f"\nMenor producción por fábrica: ")
    for i, e in enumerate(menores):
        print(f"Fabrica {i + 1}: {e} bicicletas")
    

def _menor_por_fabrica(matriz_resultado: list[list[int]]) -> list[int]:
    """
    Obtiene la producción mínima registrada por cada fábrica mediante una lista por comprensión.
    
    Pre: Recibe una lista de listas de enteros.
    
    Post: Devuelve una lista de enteros con el mínimo de cada fila.
    """
    menores = [min(fila) for fila in matriz_resultado]
    return menores

def _dia_productivo(matriz_resultado: list[list[int]], n: int) -> None:
    """
    Determina e imprime el día de la semana con mayor producción combinada entre todas las fábricas.
    
    Pre: Recibe una lista de listas de enteros y un número entero.
    
    Post: Imprime el día más productivo y su promedio.
    """
    assert n > 0 and len(matriz_resultado) == n, "N debe coincidir con la cantidad de fábricas."
    
    max_dia = 0
    promedio_produccion = 0
    for columna in range(6):
        suma_columna = 0
        for fila in range(n):
            suma_columna += matriz_resultado[fila][columna]

        promedio = suma_columna / n
        if promedio > promedio_produccion:
            promedio_produccion = promedio
            max_dia = columna
    
    print(f"El máximo día de producción fueron los dias {max_dia + 1} de la semana, con un promedio de {promedio_produccion}")

    

def _dia_mayor(matriz_resultado: list[list[int]]) -> None:
    """
    Determina e imprime cuál fue la fábrica y el día con mayor producción individual.
    
    Pre: Recibe una lista de listas de enteros.
    
    Post: Imprime el valor máximo, la fábrica y el día correspondiente.
    """
    produccion_max = 0
    fabrica = 0
    dia = 0
    for i_f, fila in enumerate(matriz_resultado):
        for i_c, columna in enumerate(fila):
            if columna > produccion_max:
                produccion_max = columna
                fabrica = i_f
                dia = i_c
    print(f"\nLa mayor producción fue de: {produccion_max}")
    print(f"Por parte de: Fábrica {fabrica + 1}")
    print(f"Día {dia + 1} de la semana")

def _suma_fabrica(matriz_resultado: list[list[int]]) -> None:
    """
    Calcula e imprime el total de bicicletas producidas por cada fábrica en la semana.
    
    Pre: Recibe una lista de listas de enteros.
    
    Post: Imprime el resultado.
    """
    print(f"\nSuma total de las fábricas: ")
    for i, fila in enumerate(matriz_resultado):
        total_fabrica = sum(fila)
        print(f"Fábrica {i + 1}: {total_fabrica} bicicletas")

def _crear_matriz(n: int) -> list[list[int]]:
    """
    Genera una matriz de fábricas y 6 días con valores aleatorios entre 0 y 150.
    
    Pre: Recibe un entero positivo mayor a cero.
    
    Post: Devuelve una matriz (lista de listas de enteros).
    """
    assert n > 0, "La cantidad de fábricas debe ser mayor a cero."
    
    matriz = []
    for fila in range(n):
        fila_actual = []
        for columna in range(6): 
            numero = random.randint(0, 150)  
            fila_actual.append(numero)
        matriz.append(fila_actual)

    return matriz

def _imprimir_matriz(matriz_resultado: list[list[int]]) -> None:
    """
    Muestra la matriz de producción por fábricas y días de la semana.
    
    Pre: Recibe una lista de listas de enteros.
    
    Post: Imprime la tabla.
    """
    print(f"\nMatriz de producción:")
    print("----------------------------------------------|")
    print("Fábrica   | LUN | MAR | MIE | JUE | VIE | SAB |")
    print("----------------------------------------------|")
    for i, fila in enumerate(matriz_resultado):
        print(f"Fábrica {i + 1} |", end="")
        for e in fila:
            print(f" {e:3} |", end="") #aca no sabia lo del e:3 para que todos los numeros ocupen el mismo espacio
        print()
    print("----------------------------------------------|")   


def main() -> None:        
    n = int(input("Ingrese la cantidad de fábricas: "))
    matriz_resultado = _crear_matriz(n)
    imprimir = _imprimir_matriz(matriz_resultado)
    _suma_fabrica(matriz_resultado)
    _dia_mayor(matriz_resultado)
    _dia_productivo(matriz_resultado, n)
    menores = _menor_por_fabrica(matriz_resultado)
    _imprimir_menores(menores)
    
if __name__ == "__main__":
    main()               

