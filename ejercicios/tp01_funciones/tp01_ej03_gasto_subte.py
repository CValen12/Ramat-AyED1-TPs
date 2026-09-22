"""
3. Una persona desea llevar el control de los gastos realizados al viajar en el
subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un
esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita
desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa
para verificar el comportamiento de la función.

Cantidad de viajes       Valor del pasaje
1 a 20                    Averiguar en Internet el valor actualizado
21 a 30                   20% de descuento sobre tarifa máxima
31 a 40                   30% de descuento sobre tarifa máxima
Más de 40                 40% de descuento sobre tarifa máxima
"""

def _monto_total(viaje: int, valor_viaje: int) -> None:
    """
    La función calcula el descuento aplicado según los viajes realizados por el usuario, hasta 20 viajes
    precio original, de 21 a 30 un 20% de descuento, de 31 a 40 un 30% de descuento, y mas de 41 un 40%.
    
    Pre: Recibe como parametro 2 enteros positivos.
    
    Post: 
    """
    contador = 1
    acumulador = 0
    for i in range(viaje):
        if contador <= 20:
            contador += 1
            acumulador += valor_viaje
        elif contador > 20 and contador <= 30:
            contador += 1
            acumulador += valor_viaje - (valor_viaje * 20 / 100)
        elif contador > 30 and contador <= 40:
            contador += 1
            acumulador += valor_viaje - (valor_viaje * 30 / 100)
        else:
            acumulador += valor_viaje - (valor_viaje * 40 / 100)
    print(f"El monto total de los {viaje} viajes es de: ${acumulador}")
    

def main() -> None:        
    _monto_total(41, 1000)
    
if __name__ == "__main__":
    main()               
            
            
            