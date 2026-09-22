"""
5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en
forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([6, 1])
retorna False. Se deberá además crear una función para verificar el comportamiento de la función.
"""

def _ordenada(lista: list[int]) -> bool:
    """
    La función recibe una lista como parámetro, crea una copia de esa lista ordenada. Si es igual a la original,
    retorna True porque está ordenada, si es distinta retorna False porque la ordenó correctamente.
    
    Pre: Recibe una lista de números enteros.
    
    Post: Retorna un booleano.
    """
    lista2 = sorted(lista)
    if lista == lista2:
        return True
    else:
        return False

def _imprimir(check: bool) -> None:
    """
    La función recibe un booleano e imprime el resultado obtenido según.
    
    Pre: Recibe un booleano
    
    Post: Imprime el resultado obtenido
    """
    if check:
        print("La lista está ordenada.")
    else:
        print("La lista NO está ordenada.")    
    
def _test_ordenada() -> None:
    """
    Ejecuta asserts para verificar el comportamiento de la función _ordenada.
    """
    assert _ordenada([1, 2, 3]) is True, "Error: [1, 2, 3] debe dar True."
    assert _ordenada([6, 1]) is False, "Error: [6, 1] debe dar False."


def main() -> None: 
    check = _ordenada([1, 2, 3])
    _test_ordenada()
    _imprimir(check)
    
if __name__ == "__main__":
    main()               