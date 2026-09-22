"""
8. La siguiente función permite averiguar el día de la semana para una fecha determi-
nada. La fecha se suministra en forma de tres parámetros enteros y la función devuel-
ve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.

"""

def _calendario(mes: int, anio: int) -> None:
    """ 
    La función imprime por completo el calendario de un mes y año recibidos como parametro.
    
    Pre: Recibe un número entero correspondiente al mes (entre 1 y 12), y otro numero entero, mayor a 0.
    
    Post: Imprime el calendario.
    """

    assert 1 <= mes <= 12, "El mes debe estar entre 1 y 12."
    assert anio > 0, "El año debe ser mayor a cero."
    
    mes_31 = [1, 3, 5, 7, 8, 10, 12]
    dia_limite = 30
    if mes in mes_31:
        dia_limite = 31
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            dia_limite = 29
        else:
            dia_limite = 28 #hasta esta parte lo saque del ejercicio 2
    dia_inicio = _diadelasemana(1, mes, anio)
    
    print("|-----------------------------------------|")
    print("| DOM | LUN | MAR | MIE | JUE | VIE | SAB |")
    print("|-----------------------------------------|")
    print("|", end= "")
    for espacio in range(dia_inicio):
        print("     |", end= "") #lo del end no lo sabia
    dia_ahora = dia_inicio
    for d in range(dia_limite):
        dia_ahora += 1
        if d < 9:
            print(f"  0{d + 1} |", end= "")
        else:
            print(f"  {d + 1} |", end= "")
        if dia_ahora % 7 == 0:
            print()
            print("|", end= "")
    print()
    print("|", end= "")
    print("-----------------------------------------|")
             
def _diadelasemana(dia: int, mes: int, anio: int) -> int:
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    año2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def main() -> None:        
    _calendario(9, 2026)   
     
if __name__ == "__main__":
    main()               
            
            
            