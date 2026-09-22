"""
5. Escribir funciones lambda para:

a. Informar si un número es oblong(o). Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo,
6 es oblongo porque resulta de multiplicar 2 * 3.

b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecutivos
comenzando desde 1. Por ejemplo 10 es un número triangular porque se obtiene
sumando 1+2+3+4.

Ambas funciones lambda reciben como único parámetro el número a evaluar y
devuelven True o False. No se permite utilizar ayudas externas a las mismas.
"""

_oblongo = lambda num: (int(num ** 0.5) * (int(num ** 0.5) + 1)) == num 

def main() -> None:    
    assert _oblongo(6) == True, "Error: 6 tiene que dar True"
    assert _oblongo(5) == False, "Error: 5 tiene que dar False"    
    num = 5
    if _oblongo(num) == True:
        print("El número es oblongo.")
    else:
        print("El número no es oblongo.")
    
if __name__ == "__main__":
    main()               
            




