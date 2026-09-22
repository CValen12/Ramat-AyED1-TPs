"""
7. Escribir una función diasiguiente(dia, mes, año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:

a. Sumar N días a una fecha.

b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""

def _dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int, int,int]:
    mes_31 = [1, 3, 5, 7, 8, 10, 12]
    dia_limite = 30
    if mes in mes_31:
        dia_limite = 31
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            dia_limite = 29
        else:
            dia_limite = 28 #hasta esta parte lo saque del ejercicio 2
    
    dia += 1
    if dia > dia_limite:
        dia = 1
        mes += 1
        if mes == 13:
            mes = 1
            anio += 1
            
    return dia, mes, anio

def _sumar_dias(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """
    La función suma una cantidad n de dias a la fecha como parámetro.
    
    Pre: Recibe como parametro 3 numero enteros positivos
    
    Post: Retorna una tupla con 3 elementos enteros
    """
    n = int(input("Ingrese el número de días a sumarle: "))
    contador = 1
    while contador != n:
        contador += 1
        dia, mes, anio = _dia_siguiente(dia, mes,anio)
    return dia, mes, anio
            

def main() -> None:
    assert _dia_siguiente(31, 12, 2023) == (1, 1, 2024), "Error: fin de año."
    assert _dia_siguiente(28, 2, 2024) == (29, 2, 2024), "Error: año bisiesto."
    
    dia, mes, anio = _dia_siguiente(31, 12, 2003)
    print(f"Día siguiente: {dia}, {mes}, {anio}")
    dia1, mes1, anio1 = _sumar_dias(dia, mes, anio)
    print(dia1, mes1, anio1)
    
if __name__ == "__main__":
    main()               
            
            
            