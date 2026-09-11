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

def crear_listas(n: int) -> list:
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

def elementos_repetidos(lista: list) -> bool:
    for e in lista:
        contador = 0
        for elem in lista:
            if e == elem:
                contador += 1
        if contador > 1:
            return True
    return False

def devolucion(valor):
    if valor == True:
        print("Hay numeros repetidos")
    else:
        print("No hay números repetidas")
        
def lista_nueva(lista: list) -> list:
    lista_nueva = sorted(lista)
    return lista_nueva
                
            
            
        


lista = crear_listas(5)
print(lista)
valor = elementos_repetidos(lista)
devolucion(valor)
lista_2 = lista_nueva(lista)
print(lista_2)
   
