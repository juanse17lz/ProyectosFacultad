
def verificar_dato_numerico(cadena:str)->bool:
    flag = True
    for digito in cadena:
        if ord(digito) < 48 or ord(digito) > 57:
            flag = False
            break
    return flag

def validar_ingreso_entero()->int:
    numero = input("Ingrese un numero entero: ")
    es_numero = verificar_dato_numerico(numero)
    while es_numero == False:
        numero = input("ERROR. Ingrese un numero entero: ")
        es_numero = verificar_dato_numerico(numero)
    numero = int(numero)
    return numero


def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int|None:
    numero = input(f"{mensaje}")
    flag = True
    contador = 1
    while flag:
        verificacion = verificar_dato_numerico(numero)
        if verificacion == False and contador < reintentos:
            contador += 1
            numero = input(f"{contador}{mensaje_error}")
        elif verificacion == True and contador < reintentos:
            numero = int(numero)
            if numero < minimo or numero > maximo:
                contador += 1
                numero = input(f"{contador}{mensaje_error}")
            else:
                retorno = numero
                flag = False
        elif contador == reintentos:
            print("Se quedo sin intententos.")
            retorno = None
            flag = False
    return retorno
    
print(get_int("Ingrese un numero entero 1 y 100: ", " intento. Error el dato ingresado es incorrecto. Ingrese un numero entero 1 y 100: ", 1, 100, 3))


