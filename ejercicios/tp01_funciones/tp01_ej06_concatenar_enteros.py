"""
6. Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite
utilizar facilidades de Python no vistas en clase.
"""

def concatenar_numeros(a: int, b: int) -> str:
    """
    La funcion recibe 2 numeros enteros y los suma, pasandolos a string, concatenandose.
    
    Pre: La funcion recibe como parametro dos numeros enteros positivos.
    
    Post: Devuelve los 2 numeros concatenados en forma de string.
    """
    resultado = str(a) + str(b)
    resultado_entero = int(resultado)
    print(f"La concatenación de estos numeros da: {resultado_entero}")
    print(type(resultado_entero))

concatenar_numeros(34, 52)
concatenar_numeros(124, 62)
