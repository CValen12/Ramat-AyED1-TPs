"""
2. Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
"""

def recibir_datos() -> tuple:
    """
    Recibe 3 numeros enteros ingresados por el usuario, correspondientes al dia, mes y año,
    y los convierte en una tupla
    
    Pre: Se le pide al usuario 3 numeros enteros positivos
    
    Post: Devuelve una tupla con los 3 elementos ingresados por el usuario
    """
    
    dia = int(input("Ingrese el número del dia: "))
    mes = int(input("Ingrese el número del mes: "))
    anio = int(input("Ingrese el número del anio: ")) 
    
    return dia, mes, anio

def verificar_datos(dia: int, mes: int, anio: int) -> bool:
    """
    Recibe como parametro 3 elemntos correspondientes al dia, mes y año y verifica si es una fecha valida.
    
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
    
def devolucion(dia: int, mes: int, anio: int) -> None:
    """ 
    Verifica si la funcion verificar_datos es true o false, e imprime en la pantalla el resultado correspondiente
    
    Pre: Una funcion con un booleano que determina si los datos son correctos.
    
    Post: Resultado que indica si la fecha es valida o no lo es.
    """
    valor = verificar_datos(dia, mes, anio)
    if valor == True:
        print("El día es una fecha valida.")
    else:
        print("El día no es una fecha valida")
        
        
mes_31 = [1, 3, 5, 7, 8, 10, 12]
dia, mes, anio = recibir_datos()
devolucion(dia, mes, anio)