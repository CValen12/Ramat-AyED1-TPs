"""
2. Escribir funciones para:

a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado.

b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La
función no debe modificar la lista.

c. Recibir una lista como parámetro y devolver una nueva lista con los elementos de la lista original,
sin importar el orden.

Combinar estas tres funciones en un mismo programa.
"""
import random

def _crear_listas(n: int) -> list[int]:
    """
    Genera una lista con n números aleatorios entre 1 y 100.
    
    Pre: Recibe un número entero mayor o igual a cero.
    
    Post: Devuelve una lista con números enteros.
    """
    assert n >= 0, "N debe ser mayor o igual a cero."
    
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

def _elementos_repetidos(lista: list[int]) -> bool:
    """
    Verifica si existen elementos repetidos en una lista.
    
    Pre: Recibe una lista de enteros.
    
    Post: Devuelve True si hay repetidos, False en caso contrario. Un booleano.
    """
    for e in lista:
        contador = 0
        for elem in lista:
            if e == elem:
                contador += 1
        if contador > 1:
            return True
    return False

def _devolucion(valor: bool) -> None:
    """
    Muestra por pantalla si se encontraron elementos duplicados.
    
    Pre: Recibe un booleano.
    
    Post: Imprime el resultado.
    """
    if valor == True:
        print("Hay números repetidos")
    else:
        print("No hay números repetidos")
        
def _lista_nueva(lista: list[int]) -> list[int]:
    lista_nueva = sorted(lista)
    return lista_nueva
                
def main() -> None:       
    assert _elementos_repetidos([1, 2, 3, 2]) is True, "Error: debe detectar repetidos."
    
    lista = _crear_listas(5)
    print(lista)
    valor = _elementos_repetidos(lista)
    _devolucion(valor)
    lista_2 = _lista_nueva(lista)
    print(lista_2)
    
if __name__ == "__main__":
    main()                           
            
