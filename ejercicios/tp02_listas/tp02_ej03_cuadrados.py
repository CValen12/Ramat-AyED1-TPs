"""
3. Crear una lista con los cuadrados de los números enteros entre 1 y N (ambos incluidos), donde N se
ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.
"""

def _lista_enteros() -> list[int]:
    """
    Esta funcón crea una lista de números al cuadrado entre 1 y N, N corresponde al número que ingrese el usuario.
    
    Pre: None
    
    Post: Retorna una lista con elementos enteros
    """
    longitud = int(input("Ingrese el límite máximo de la lista: "))
    lista = []
    numero = 0
    for i in range(longitud):
        numero += 1
        lista.append(numero ** 2)
    print(lista)
    return lista

def _imprimir_ultimos(lista: list[int]) -> None:
    """
    La función agarra una lista e imprime los utlimos 10 elementos, si no los hay, imprime los últimos.
    
    Pre: Recibe una lista de elementos enteros.
    
    Post: Imprime los últimos 10 elementos.
    """
    contador = 0
    for i in reversed(lista):
        print(i)
        contador += 1
        if contador == 10:
            break

def main() -> None:      
    assert [i ** 2 for i in range(1, 6)] == [1, 4, 9, 16, 25], "Error en los cuadrados."  
    lista = _lista_enteros()
    _imprimir_ultimos(lista)
    
if __name__ == "__main__":
    main()               
