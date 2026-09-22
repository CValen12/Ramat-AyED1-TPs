"""
5. Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:

mostrar_butacas:
Mostrar por pantalla el estado de cada una de las butacas del cine. Esta función se
deberá ser invocada antes de que se realice la reserva, y se volverá a invocar luego
de la misma con los estados actualizados.

reservar:
Deberá recibir una matriz y la butaca seleccionada, y actualizar la sala en caso de
estar disponible dicha butaca. La función devolverá True/False según lo reserve la
butaca.

cargar_sala:
Recibirá una matriz como parámetro y la cargará con valores aleatorios para simular
una sala con butacas ya reservadas.

butacas_libres:
Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la
sala.

butacas_contiguas:
Buscará en la secuencia más larga de butacas libres contiguas en una misma fila y
devolverá las coordenadas de inicio de la misma.
"""

def _pedir_reserva() -> tuple[int, int]:
    """
    Solicita al usuario la fila y la butaca a reservar.
    
    Pre: None.
    
    Post: Retorna una tupla de 2 elementos enteros.
    """
    fila = int(input("Ingrese la fila que desee: "))
    butaca = int(input("Ingrese la butaca que desee: "))
    return fila, butaca
    
def _reservar(matriz_cine: list[list], fila: int, butaca: int) -> bool:
    """
    Busca el elemento de la lista indicados según fila y butaca, si es 0, lo cambia a 1 y retorna True.
    
    Pre: Recibe una lista de listas de enteros.
    
    Post: Devuelve un booleano.
    """
    fila_selec = fila - 1
    butaca_selec = butaca - 1
    if 0 <= fila_selec < len(matriz_cine) and 0 <= butaca_selec < len(matriz_cine[0]):
        if matriz_cine[fila_selec][butaca_selec] == 0:
            matriz_cine[fila_selec][butaca_selec] = 1  
            return True
        
    return False #esto no lo sabia aplicar, si se incumple cualquiera de las 2 opciones retorna false
    

def _mostrar_butacas(matriz_cine: list[list]) -> None:
    """
    Muestra en pantalla el estado actual de las butacas de la sala (1: Ocupado/ 0: Libre).
    
    Pre: Recibe una lista de listas de enteros.
    
    Post: Imprime la sala como una tabla.
    """
    print(f"\nButacas disponibles (0- Libre / 1- Ocupado):")
    print("----------------------------------------------")
    for i, fila in enumerate(matriz_cine):
        print(f"Fila {i + 1}:|", end="")
        for e in fila:
            print(f" {e} |", end="")
        print()
    print("----------------------------------------------") 

def _crear_matriz(filas: int, butacas: int) -> list[list[int]]:
    """
    Crea una matriz inicializada en 0 (asiento libre) según filas y butacas dadas.
    
    Pre: Recibe 2 números enteros mayores a cero.
    
    Post: Retorna la matriz con todos los elementos en 0.
    """
    assert filas > 0 and butacas > 0, "Dimensiones inválidas."
    
    matriz = []
    for fila in range(filas):
        fila_actual = []
        for columna in range(butacas): 
            numero = 0 
            fila_actual.append(numero)
        matriz.append(fila_actual)

    return matriz

def _tamaño_cine() -> tuple[int, int]:
    """
    Pide al usuario la cantidad de filas y butacas del cine.
    
    Pre: None.
    
    Post: Retorna una tupla de  2 elementos enteros.
    """
    filas = int(input("Ingrese la cantidad de filas: "))
    butacas = int(input("Ingrese la cantidad de butacas por fila: "))
    return filas, butacas
    

def _mostrar_opciones() -> None:
    """
    Muestra las opciones del menú por pantalla.
    
    Pre: None.
    
    Post: Imprime las opciones.
    """
    print("\nBienvenido.")
    print()
    print("1- Mostrar butacas.")
    print("2- Reservar.")
    print("3- Sala simulada.")
    print("4- Cantidad butacas disponibles.")
    print("5- Cantidad butacas contiguas.")
    print("6- Salir del menú")

def _menu() -> None:
    """
    Menu para navegar en las opciones seleccionadas por el usuario.
    
    Pre: None.
    
    Postcondiciones: Imprime y deja seleccionar opciones
    """
    filas, butacas = _tamaño_cine()
    matriz_cine = _crear_matriz(filas, butacas)
    _mostrar_opciones()
    opcion = ""
    while opcion != "6":
        opcion = input("\nSeleccione el número de opción: ")
        if opcion == "1":
            _mostrar_butacas(matriz_cine)        
        elif opcion == "2":
            fila, butaca = _pedir_reserva()
            dato = _reservar(matriz_cine, fila, butaca)
            if dato == True:
                print("La reserva fue realizada con éxito!")
                _mostrar_butacas(matriz_cine)
            else:
                print("La butaca seleccionada ya esta elegida o esta fuera del rango disponible.")
                
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("La opción seleccionada no es una opción valida.")   
            
def main() -> None:        
    _menu()
    
if __name__ == "__main__":
    main()               
_menu()