"""
4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a
falta de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

billetes = [5000, 1000, 500, 200, 100, 50, 10]


def sacar_resto() -> int:
    """
    El usuario ingresa el monto total de la compra y el monto que paga el cliente. Este se resta para determinar
    el monto que hay que devolverle al cliente.

    Pre: Ingreso de 2 numeros enteros positivos. Donde lo que paga el cliente debe ser mayor al monto de la compra.

    Post: Retorna un numero entero positivo.
    """
    costo = int(input("Ingrese el valor total de la compra: "))
    while costo < 0:
        print("Ingrese un número valido.")
        costo = int(input("Ingrese el valor total de la compra: "))

    cliente = int(input("Ingrese el monto que pago el consumidor: "))
    while cliente < costo:
        print("El pago del cliente no alcanza el monto de la compra.")
        cliente = int(input("Ingrese el monto que pago el consumidor: "))

    vuelto = abs(costo - cliente)
    return vuelto


def monto_a_devolver(vuelto: int) -> tuple[list[int], int]:
    """
    Se recibe un numero entero que corresponde al vuelto. Se recorre la lista global de billetes y busca
    la cantidad optima de billetes que debe recibir el cliente. Se crea una lista con las cantidades. Y un
    numero entero que indica el restante final que no se puede devolver con los billetes que hay.

    Pre: Un numero entero correspondiente al dinero que se le debe devolver al cliente

    Post: Retorna una lista con las cantidades que debe recibir el cliente, alineando los indices con la lista de billetes.
    Y un numero entero que corresponde al vuelto final que no es posible devolver.
    """
    cantidad_billetes = []
    for b in billetes:
        cantidad = vuelto // b
        cantidad_billetes.append(cantidad)
        vuelto = vuelto % b
    vuelto_final = vuelto
    return cantidad_billetes, vuelto_final


def devolucion(cantidad_billetes: list[int], vuelto: int, vuelto_final: int) -> None:
    """
    Se imprime en pantalla el monto total a devolver. La cantidad de billetes de cada valor a devolver.
    Y el monto total que no se puede devolver, en caso de este no sea 0.

    Pre: Recibe la lista de cantidad de billetes de cada valor, usa la lista de billetes. Y 2 numeros enteros,
    uno que indica el vuelto total, y otra el vuelto que no es posible regresar.

    Post: Se imprime el monto a devolver total, la cantidad de billetes, y en caso de que no se pueda regresar
    una parte, el monto que no es posible.
    """
    print(f"El monto a devolver es: ${vuelto}")
    for i, e in enumerate(cantidad_billetes):
        if e > 0:
            print(f"{e} billetes de ${billetes[i]}")
    if vuelto_final > 0:
        print(f"Hay ${vuelto_final} que no es posible devolver.")


vuelto = sacar_resto()
cantidad_billetes, vuelto_final = monto_a_devolver(vuelto)
devolucion(cantidad_billetes, vuelto, vuelto_final)
