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