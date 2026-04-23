def insertar_entero()->int:
    """Recibe un numero entero y lo retorna.

    Returns:
        Int: retorna el numero entero validado.
    """
    numero = int(input("Ingrese un numero entero: "))
    if numero > 0:
        return numero
    else:
        print("El numero no es entero.")