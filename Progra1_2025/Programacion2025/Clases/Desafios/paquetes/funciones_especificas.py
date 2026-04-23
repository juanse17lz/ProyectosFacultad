def determinar_parimpar(numero:int)->bool:
    """Determina si el numero ingresado es par o impar. Si es par retorna "True", si es impar retorna "False".

    Args:
        numero (int): numero a determinar si es par o impar.

    Returns:
        Bool: "True" si es par, "False" si es impar
    """
    verificacion = False
    if numero % 2 == 0:
        verificacion = True
    return verificacion

def definir_mayor(primero:int,segundo:int,tercero:int)->int:
    """Recibe tres numeros y retorna cual de los tres numeros ingresados es el mayor.

    Args:
        primero (int): primer numero ingresado.
        segundo (int): segundo numero ingresado.
        tercero (int): tercer numero ingresado.

    Returns:
        int: mayor numero ingresado
    """
    mayor = 0
    for i in range(3):
        if primero > mayor:
            mayor = primero
        elif segundo > mayor:
            mayor = segundo
        elif tercero > mayor:
            mayor = tercero
    return mayor

def verificar_primo(numero:int)->bool:
    """Verifica si un numero es primo o no.

    Args:
        numero (int): Numero a verificar.

    Returns:
        bool: "True" si es primo, "False" si no es primo.
    """
    contador = 0
    for i in range(numero):
        if numero%(i+1) == 0:
            contador += 1
    if contador > 2:
        retorno = False
    else:
        retorno = True
    return retorno

def verificar_dato_numerico(cadena:str)->bool:
    """Determina si los digitos de una cadena son de tipo numerico o no.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        bool: Retorna True si todos los digitos de la cadena son de tipo numerico, caso contrario retorna False.
    """
    flag = True
    for digito in cadena:
        if ord(digito) == 45 or (ord(digito) >= 48 and ord(digito) <= 57):
            flag = False
            break
    return flag

def insertar_entero_validado(mensaje:str,mensaje_error:str)->int:
    """Pide que se ingrese un dato y verifica si es de tipo numerico, caso contrario lo vuelve a pedir hasta que se ingrese un dato de tipo numerico.

    Returns:
        int: Retorna el numero validado.
    """
    numero = input(mensaje)
    es_numero = verificar_dato_numerico(numero)
    while es_numero == False:
        numero = input(mensaje_error)
        es_numero = verificar_dato_numerico(numero)
    return int(numero)