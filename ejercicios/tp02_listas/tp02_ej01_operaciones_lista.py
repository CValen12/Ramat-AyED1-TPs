"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su
funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un
número al azar de dos dígitos.

b. Calcular y devolver el producto de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa
desde el teclado y la función lo recibe como parámetro. No utilizar listas auxiliares.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo
de lista capicúa es [50, 17, 91, 17, 50].
"""
import random 

def _cuatro_digitos_random() -> list[int]:
    """
    La función crea una lista con una longitud entre 10 y 99 al azar, donde cada uno de estos elementos
    es un número al azar entre 1000 y 9999
    
    Pre: None
    
    Post: Retorna una lista.
    """
    lista = []
    longitud = random.randint(10, 99)
    for i in range(longitud):
        lista.append(random.randint(1000, 9999))
    print(lista)
    print(len(lista))
    return lista

def _producto_lista(lista: list[int]) -> int:
    """
    La función toma los elementos de la lista y los multiplica entre sí, es decir, calcula el producto.
    
    Pre: Recibe una lista.
    
    Post: Imprime el resultado
    """
    assert len(lista) > 0, "La lista no puede estar vacía."
    
    producto = 1
    for i in lista:
        producto *= i
    return producto

def main() -> None:        
    assert _producto_lista([2, 3, 4]) == 24, "Error en producto."
    
    lista = _cuatro_digitos_random()
    producto = _producto_lista(lista)   
    print(f"El producto de la lista es {producto}")
    
if __name__ == "__main__":
    main()               