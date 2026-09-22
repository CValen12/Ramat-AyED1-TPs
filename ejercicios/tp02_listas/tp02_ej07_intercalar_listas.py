"""
7. Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse
exactamente mientras tengan elementos de las listas, si una lista nueva que no se modificará la primera.
Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].
Las listas pueden tener distintas longitudes.
"""

def _intercalar_listas(lista1: list[int], lista2: list[int]) -> list[int]: 
    """
    La función toma 2 listas. Crea un bucle donde va tomando el índice de cada una de las listas y
    agrega el elemento del índice de a uno por vez a una tercera lista. El bucle se rompe cuando el índice
    supera a las 2 listas.
    
    Pre: None
    
    Post: Retorna una lista con elementos enteros
    """
    lista3 = []
    
    indice = 0
    while indice < len(lista1) or indice < len(lista2):
        if indice < len(lista1):
            lista3.append(lista1[indice])
        if indice < len(lista2):
            lista3.append(lista2[indice])
        indice += 1
    return lista3
        
def main() -> None:
    assert _intercalar_listas([8, 1, 3], [5, 9, 7]) == [8, 5, 1, 9, 3, 7], "Error al intercalar."
    
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6, 7]       
    lista3 = _intercalar_listas(lista1, lista2)
    print(lista3)
    
if __name__ == "__main__":
    main()                

