"""
1. Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
"""

def _recibir_numero() -> list[int]:
    """
    Se le pide al usuario tres números y los agrega a una lista.
    
    Pre: Los números ingresados deben ser enteros positivos
    
    Post: Se retorna a una lista con 3 elementos enteros
    """
    lista = []
    contador = 0
    while contador != 3:
        numero = int(input("Ingrese un número: "))
        if numero > -1:
            contador += 1
            lista.append(numero)
        else:
            print("\nIngrese un número válido")
    return lista

def _encontrar_mayor(lista: list[int]) -> int:
    """
    Recorre la lista hasta encontrar el mayor elemento
    
    Pre: Se requiere como parametro la lista de 3 elementos enteros.
    
    Post: Se retorna un número entero.
    """
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
    return mayor

def _verificar_unico(lista: list[int], mayor: int) -> bool:
    """
    Recorre la lista original y la compara con el número mayor buscando si se repite.
    
    Pre: Recibe la lista de 3 elementos y el número entero mayor de la lista.
    
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
    
def _devolucion(lista: list[int], mayor: int, unico: bool) -> None:
    """
    Imprime en pantalla el resultado. En caso de haber un número mayor unico, lo imprime en pantalla. Y si no
    imprime que no lo hay
    
    Pre: Recibe si el número mayor es unico o no.
    
    Post: Imprime el resultado del número mayor unico.
    """
    if unico == True:
        print(f"El mayor único número ingresado es: {mayor}")
    else:
        print("No hay un número mayor único.")
        
def main() -> None:        
    lista = _recibir_numero()
    mayor = _encontrar_mayor(lista)
    unico = _verificar_unico(lista, mayor)
    _devolucion(lista, mayor, unico)
    
if __name__ == "__main__":
    main()

