"""
9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos
de 5. A y B se ingresan desde el teclado.
"""

def _ingreso_numeros() -> tuple[int, int]:
    """
    La función le pide al usuario 2 números enteros positivos que determinarán los límites de una futura
    lista por comprensión
    
    Pre: None
    
    Post: Retorna una tupla con elementos enteros.
    """
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

def _lista_multiplos7(num1: int, num2: int) -> None:
    """
    Genera e imprime los múltiplos de 7 que no sean múltiplos de 5 entre 2 números enteros.
    
    Pre: Recibe 2 números enteros.
    
    Post: Imprime la lista resultante.
    """
    assert num1 <= num2, "El límite inferior no puede ser mayor al superior."
    
    lista = [n for n in range(num1, num2) if n % 7 == 0 and n % 5 != 0]
    print(lista)

def main() -> None:        
    num1, num2 = _ingreso_numeros()
    _lista_multiplos7(num1, num2)
    
if __name__ == "__main__":
    main()               

