'''
1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
4) Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
5) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
6) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
7) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
8) Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
9) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
10) Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
11) Crear una función que imprima la tabla de multiplicar ded un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es el 1 al 10.
12) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
'''

#1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def insertar_entero()->int:
    """Recibe un numero entero y lo retorna.

    Returns:
        Int: retorna ek numero entero validado.
    """
    numero = int(input("Ingrese un numero entero: "))
    if numero > 0:
        return numero
    else:
        print("El numero no es entero.")

#insertar_entero()

#2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def insertar_flotante()->float:
    """Recibe un numero y lo convierte en flotante.

    Returns:
        Float: retorna el numero recibido convertido en flotante.
    """
    numero = float(input("Ingrese un numero flotante: "))
    return numero

#insertar_flotante()

#3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def ingresar_cadena()->str:
    """Permite recibir una cadena y la retorna.

    Returns:
        Str: retona la cadena ingresada.
    """
    cadena = input("Ingrese una cadena: ")
    return cadena

def area_rectangulo(base:int,altura:int)->int:
    """Permite calcular el area de un rectangulo.

    Args:
        base (int): Base del rectangulo.
        altura (int): Altura del rectangulo.

    Returns:
        Int: retorna el area del rectangulo.
    """
    return base * altura

#print(ingresar_cadena())
#print(area_rectangulo(25,10))

#4) Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio:int)->int:
    """Calcula el area de un circulo.

    Args:
        radio (int): Radio de un circulo

    Returns:
        Int: Retorna el area del circulo.
    """
    return 3.14 * (radio * radio)

#print(area_circulo(7))

#5) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def imprimir_parimpar(numero:int):
    """Determina si el numero ingresado es primo o no y lo imprime en pantalla.

    Args:
        numero (int): numero a verificar.
    """
    if numero % 2 == 0:
        print(f"El numero {numero} es par.")
    else:
        print(f"El numero {numero} es impar.")

#imprimir_parimpar(22)

#6) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

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

'''
numero = determinar_parimpar(1597863213)
if numero == True:
    print("Es par")
else:
    print("Es impar")
'''

#7) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

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

#print(definir_mayor(5,3,4))

#8) Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def numero_potenciado(base:int,exponente:int)->int:
    """Calcula la potencia de un numero.

    Args:
        base (int): Numero a ponteciar.
        exponente (int): Potencia a calcular.

    Returns:
        int: Resultado de la potenciacion.
    """
    resultado = 0
    for i in range(exponente):
        if resultado == 0:
            resultado += base
        else:
            resultado *= base
    return resultado

# print(numero_potenciado(4,4))

#9) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

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

# print(verificar_primo(97))

#10) Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def mostrar_cantidad_primos(numero:int):
    """Muestra la cantidad de numeros primos que hay desde el 0 hasta el numero ingresado.

    Args:
        numero (int): numero hasta el que se van a contabilizar los numeros primos.
    """
    for j in range(numero):
        contador = 0
        for i in range(j+1):
            if (j+1) % (i+1) == 0:
                contador += 1
        if contador == 2:
            print(j+1)

# mostrar_primos(100)

#11) Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def mostrar_tabla(numero:int, largo=10):
    """Muestra la tabla de multiplicar de un numero. Por defecto hasta 10.

    Args:
        numero (int): Numero del que se mostrara la tabla.
        largo (int, optional): Longitud que tendra la tabla. Por defecto hasta 10.
    """
    for i in range(largo):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

# mostrar_tabla(5,20)

#12) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
#1.12) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def verificar_dato_numerico(cadena:str)->bool:
    flag = True
    for digito in cadena:
        if ord(digito) < 48 or ord(digito) > 57:
            flag = False
            break
    return flag

def insertar_entero_validado()->str:
    numero = input("Ingrese un numero entero: ")
    es_numero = verificar_dato_numerico(numero)
    while es_numero == False:
        numero = input("ERROR. Ingrese un numero entero: ")
        es_numero = verificar_dato_numerico(numero)
    return numero


#print(insertar_entero_validado())

#2.12) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def verificar_dato_flotante(cadena:str)->bool:
    flag = True
    for digito in cadena:
        if len(cadena) == 1 and ord(cadena) == 46:
            flag = False
            break
        elif ord(digito) == 46 or (ord(digito) >= 48 or ord(digito) <= 57):
            flag = True
        else:
            flag = False
            break
    return flag

def insertar_flotante_validado()->float:
    numero = input("Ingrese un numero flotante: ")
    es_flotante = verificar_dato_flotante(numero)
    while es_flotante == False:
        numero = input("ERROR. Ingrese un numero flotante: ")
        es_flotante = verificar_dato_flotante(numero)
    numero = float(numero)
    return numero

print(insertar_flotante_validado())



#3.12) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def verificar_mayuscula(cadena:str)->bool:
    mayuscula = True
    for digito in cadena:
        if ord(digito) < 65 or ord(digito) > 90:
            mayuscula = False
            break

    return mayuscula

def verificar_minuscula(cadena:str)->bool:
    minuscula = True
    for digito in cadena:
        if ord(digito) < 97 or ord(digito) > 122:
            minuscula = False
            break

    return minuscula

def insertar_cadena_validado()->str:
    cadena = input("Ingrese un cadena: ")
    minuscula = verificar_minuscula(cadena)
    mayuscula = verificar_mayuscula(cadena)
    while minuscula == False or mayuscula == False:
        cadena = input("ERROR. Ingrese un cadena: ")
        minuscula = verificar_minuscula(cadena)
        mayuscula = verificar_mayuscula(cadena)
    return cadena

#print(insertar_cadena_validado())


def area_rectangulo(base:int,altura:int):
    return base * altura

def calculadora_basica(numero:int,numero_operador:int,operacion:str="suma")->float:
    """Calculadora que puede realizar 4 operaciones(suma, resta, multiplicacion, division).

    Args:
        numero (int): Numero a operar.
        numero_operador (int): Numero operador.
        operacion (str, optional): Opreacion que se desea realizar. Defaults to "suma".

    Returns:
        float: Devuelve el resultado de la operacion realizada.
    """
    
    match operacion:
        case "suma":
            resultado = numero + numero_operador
        case "resta":
            resultado = numero - numero_operador
        case "multiplicacion":
            resultado = numero * numero_operador
        case "division":
            resultado = numero / numero_operador
    return resultado
    
# print(calculadora_basica(25,2,"division"))

def sumar(sumando:int,sumando_2:int)->float:
    resutaldo = sumando + sumando_2
    return resutaldo

def resta(minuendo:int,sustraendo:int)->float:
    resutaldo = minuendo - sustraendo
    return resutaldo

def multiplicacion(factor:int,factor_2:int)->float:
    resutaldo = factor * factor_2
    return resutaldo

def division(dividendo:int,divisor:int)->float:
    if divisor == 0:
        print("No se puede realizar esta operacion.")
    resutaldo = dividendo / divisor
    return resutaldo

def porcentaje(total:int,porcentaje:int)->float:
    if porcentaje == 0:
        print("No se puede realizar esta operacion.")
    resultado = (porcentaje/total) * 100
    return resultado

def potenciacion(base:int,exponente:int)->float:
    resultado = 0
    if exponente == 0:
        resultado = 1
    else:
        for i in range(exponente):
            if resultado == 0:
                resultado = base
            else:
                resultado *= base
    return resultado

def validar_tipo(variable,tipo)->bool:
    if type(variable) == tipo:
        retorno = True
    else:
        retorno = False
    return retorno
    
def imprimir_elementos_cadena(cadena):
    for i in cadena:
        print(i)

#imprimir_elementos_cadena("Hola como estas.")
