"""
9. Resolver el siguiente problema utilizando funciones:

Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.

Además, se desea saber cuántos camiones se necesitan para transportar la cose-
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no será despachado por su alto costo.
"""

import random

def _reparto(naranjas: int) -> tuple[int, int, int, list[int]]:
    """
    Simula la cosecha de la cantidad de naranjas ingresada, clasifica para jugo o cajón y calcula sobrantes.
    
    Pre: Recibe un número entero mayor a 0.
    
    Post: Devuelve tupla con (jugo, cajones, sobrante, lista_pesos_cajones), 3 enteros y una lista.
    """
    assert naranjas >= 0, "La cantidad de naranjas no puede ser negativa."
    
    naranjas_cajon = 0
    naranjas_jugo  = 0
    cajones = 0
    sobrante = 0
    peso_cajon = 0
    cajones_pesos_lista = []
    
    for i in range(naranjas):
        peso = random.randint(150, 350)
        
        if peso >= 200 and peso <= 300:
            naranjas_cajon += 1
            peso_cajon += peso
            if naranjas_cajon == 100:
                cajones += 1
                cajones_pesos_lista.append(peso_cajon)
                naranjas_cajon = 0
                peso_cajon = 0
        else:
            naranjas_jugo += 1
        
    sobrante = naranjas_cajon
    return naranjas_jugo, cajones, sobrante, cajones_pesos_lista
    
def _calcular_camiones(cajones_pesos_lista: list[int]) -> tuple[int, int]:
    """
    Calcula la cantidad de camiones despachados según el peso de los cajones.
    
    Pre: Recibe una lista que debe contener enteros positivos.
    
    Post: Devuelve tupla con 2 elementos enteros positivos.
    """
    assert isinstance(cajones_pesos_lista, list), "Debe ser una lista."
    
    peso_camion = 0
    camiones = 0
    sobrante_camion = 0
    for p in cajones_pesos_lista:
        if peso_camion + p < 500000:
            peso_camion += p
        else:
            camiones += 1
            print(f"Camión {camiones}: {peso_camion} kg")
            peso_camion = 0
    if peso_camion < 400000:
        sobrante_camion = peso_camion
        print(f"Un camión no salió por su peso de: {sobrante_camion}")
    else:
        camiones += 1
        print(f"Camión {camiones}: {peso_camion} kg")
        
    return camiones, sobrante_camion
        
def main() -> None:
    n = int(input("Ingrese la cantidad de naranjas cosechadas: "))

    naranjas_jugo, cajones, sobrante, cajones_pesos_lista = _reparto(n)
    camiones, sobrante_camion = _calcular_camiones(cajones_pesos_lista)


    print(f"\nCajones llenos: {cajones}")
    print(f"Naranjas para jugo: {naranjas_jugo}")
    print(f"Sobrante naranjas: {sobrante}")
    print(f"Camiones: {camiones}")
    
if __name__ == "__main__":
    main()                    
        

        