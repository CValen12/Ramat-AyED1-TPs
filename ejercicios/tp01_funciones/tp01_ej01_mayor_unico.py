"""
1. Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
"""

def recibir_numero() -> list:
    """
    Se le pide al usuario tres números y los agrega a una lista.
    
    Pre: Los numeros ingresados deben ser enteros positivos
    
    Post: Se retorna a una lista con 3 elementos
    """
    lista = []
    contador = 0
    while contador != 3:
        numero = int(input("Ingrese un número: "))
        if numero > -1:
            contador += 1
            lista.append(numero)
        else:
            print("\nIngrese un número valido")
    return lista

def encontrar_mayor(lista: list) -> int:
    """
    Recorre la lista hasta encontrar el mayor elemento
    
    Pre: Se requiere como parametro la lista de 3 elementos enteros.
    
    Post: Se retorna un numero entero.
    """
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor

def verificar_unico(lista: list, mayor: int) -> bool:
    """
    Recorre la lista original y la compara con el numero mayor buscando si se repite.
    
    Pre: Recibe la lista de 3 elementos y el numero entero mayor de la lista.
    
    Post: Retorna true si el elemento mayor se repite, y false si no se repite
    """
    
    contador = 0
    for n in lista:
        if n == mayor:
            contador += 1
    if contador == 1:
        return True
    else:
        return False
    
def devolucion(lista: list, mayor: int, unico: bool) -> None:
    """
    Imprime en pantalla el resultado. En caso de haber un numero mayor unico, lo imprime en pantalla. Y si no
    imprime que no lo hay
    
    Pre: Recibe si el numero mayor es unico o no.
    
    Post: Imprime el resultado del numero mayor unico.
    """
    verificar_unico(lista, mayor)
    if unico == True:
        print(f"El mayor único número ingresado es: {mayor}")
    else:
        print("No hay un número mayor único.")
        
lista = recibir_numero()
mayor = encontrar_mayor(lista)
unico = verificar_unico(lista, mayor)
devolucion(lista, mayor, unico)