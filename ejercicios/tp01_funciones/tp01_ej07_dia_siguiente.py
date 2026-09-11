"""
7. Escribir una función diasiguiente(dia, mes, año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:

a. Sumar N días a una fecha.

b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""

""" Las proxima funcion la saque del ejercicio N° 2"""

def verificar_datos(dia: int, mes: int, anio: int) -> bool:
    """
    Recibe como parametro 3 elementos correspondientes al dia, mes y año y verifica si es una fecha valida.
    
    Pre: Recibe 3 numeros enteros.
    
    Post: Devuelve un booleano. True si es una fecha valida, False si no lo es.
    """
    dia_limite = 30
    if mes in mes_31:
        dia_limite = 31
    elif mes == 2:
        if anio % 4 == 0 and anio % 100 != 0:
            dia_limite = 29
        elif anio % 400 == 0:
            dia_limite = 29
        else:
            dia_limite = 28
    else:
        dia_limite = 30
        
    if dia > 0 and dia <= dia_limite:
        if mes > 0 and mes <= 12:
            if anio > 0 and anio <= 2027:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def dia_siguiente(dia: int, mes: int, anio: int):
    
datos = verificar_datos(31, 12, 2023)
dia_siguiente()