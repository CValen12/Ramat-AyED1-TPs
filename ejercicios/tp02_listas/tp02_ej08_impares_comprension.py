"""
8. Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares
comprendidos entre 100 y 200.
"""

def _lista_impares() -> list[int]:
    """
    La función utiliza una lista por comprensión para que los elementos de la lista sean números impares entre
    100 y 200.
    
    Pre: None
    
    Post: Lista de números enteros.
    """
    lista = [n for n in range(100, 200) if n % 2 == 1]
    print(lista)
    return lista

def main() -> None:        
    _lista_impares()
    
if __name__ == "__main__":
    main()               

