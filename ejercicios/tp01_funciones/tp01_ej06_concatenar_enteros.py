"""
6. Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite
utilizar facilidades de Python no vistas en clase.
"""

def _concatenar_numeros(a: int, b: int) -> None:
    """
    La función recibe 2 números enteros y los suma, pasandolos a string, concatenandose. Después se
    pasan a int para darles valor.
    
    Pre: La función recibe como parámetro dos números enteros positivos.
    
    Post: Devuelve los 2 números concatenados en forma de entero.
    """
    assert a > 0 and b > 0, "Ambos números deben ser enteros positivos."
    resultado = str(a) + str(b)
    resultado_entero = int(resultado)
    return resultado_entero

def main() -> None:
    assert _concatenar_numeros(1234, 567) == 1234567, "Error: debe dar 1234567."
    assert _concatenar_numeros(34, 52) == 3452, "Error: debe dar 3452."    
    resultado_entero = _concatenar_numeros(34, 52)
    print(resultado_entero)
    
if __name__ == "__main__":
    main()               
            
