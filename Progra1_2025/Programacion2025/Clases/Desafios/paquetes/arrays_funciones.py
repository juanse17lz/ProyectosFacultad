from paquetes.funciones_especificas import *
'''
1- Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
2- Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
3- Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
4- Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
5- Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
6- Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
7- Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
8- Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
 a- Una lista de nombres (lista_nombres).
 b- Un nombre a buscar en la lista (nombre_antiguo).
 c- Un nombre de reemplazo (nombre_nuevo).
 La función debe realizar las siguientes acciones:
 Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
 Retornar la cantidad total de reemplazos realizados.
9- Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la intersección de los dos arrays.
10- Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la unión de los dos arrays.
11- Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la diferencia de los dos arrays.
'''
#1- Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(longitud:int)->list:
    """Crea una lista de elementos vacios con la longitud del parametro ingresado.

    Args:
        longitud (int): longitud de la lista.

    Returns:
        list: lista de elementos vacios con la longitud ingresada.
    """
    lista = []
    for i in range(longitud):
        lista.append("")
    return lista

#print(len(crear_array(10)))

#2- Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
def crear_array_numeros_validados(longitud:int,mensaje:str,mensaje_error:str,minimo:int,maximo:int)->list:
    """Crea una lista que permite ingresar la cantidad de numeros deseados por parametro:

    Args:
        longitud (int): Cantidad de numeros a pedir.
        mensaje (str): Mensaje que se mostrara en pantalla.
        mensaje_error (str): Mensaje que se mostrara en pantalla en caso de error.
        minimo (int): Valor minimo a ingresar.
        maximo (int): Valor maximo a ingresar.

    Returns:
        list: Lista con los numeros ingresados por el usuario.
    """
    lista = crear_array(longitud)
    for i in range(len(lista)):
        numero = insertar_entero_validado(mensaje,mensaje_error)
        while numero < minimo or numero > maximo:
            print("Numero fuera de rango")
            numero = insertar_entero_validado(mensaje,mensaje_error)
        lista[i] = numero
    return lista


#print(crear_array_numeros(10))

#3- Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
def calcular_promedios_lista(lista:list)->int:
    """Calcula el promedio de los numeros de una lista.

    Args:
        lista (list): Lista con elementos tipo "int".

    Returns:
        int: Promedio de los numeros de la lista.
    """
    acumulador = 0
    contador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
        contador += 1
    resultado = acumulador / contador
    return resultado

notas = [1,2,3,-4,3]
#print(calcular_promedios_lista(notas))

#4- Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def calcular_promedios_positivos(lista:list)->int:
    """Calcula el promedio de los numero positivos de una lista.

    Args:
        lista (list): Lista de elementos tipo "int".

    Returns:
        int: Promedio de los elementos positivos de la lista.
    """
    acumulador = 0
    contador = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            acumulador += lista[i]
            contador += 1
    resultado = acumulador / contador
    return resultado

#print(calcular_promedios_positivos(notas))

#5- Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def calcular_producto_lista(lista:list)->int:
    """Calcula el producto de los elementos de una lista.

    Args:
        lista (list): Lista de elementos tipo "int".

    Returns:
        int: Producto de elementos de la lista.
    """
    acumulador = 0
    contador = 0
    for i in range(len(lista)):
        if acumulador == 0:    
            acumulador += lista[i]
            contador += 1
        else:
            acumulador *= lista[i]
            contador += 1
    return acumulador

#print(calcular_producto_lista(notas))

#6- Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def maximo_lista(lista:list)->int:
    """Busca y retorna el elmento con mayor valor de una lista.

    Args:
        lista (list): Lista de elementos tipo "int".

    Returns:
        int: Elemento de maximo de valor de la lista.
    """
    flag = False
    maximo = None
    for i in range(len(lista)):
        if flag == False:
            maximo = lista[i]
            flag = True 
        else:
            if lista[i] > maximo:
                maximo = lista[i]
    return maximo

#print(maximo_lista(notas))

#7- Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
def maximos_pos_lista(lista:list):
    """Imprime la posicion de elementos que tengan el valor maximo en la lista.

    Args:
        lista (list): Lista de elementos tipo "int".
    """
    maximo = maximo_lista(lista)
    for i in range(len(lista)):
        if lista[i] == maximo:
            print(f"Posicion de la lista: {i}")

#maximos_pos_lista(notas)

'''
8- Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
 a- Una lista de nombres (lista_nombres).
 b- Un nombre a buscar en la lista (nombre_antiguo).
 c- Un nombre de reemplazo (nombre_nuevo).
 La función debe realizar las siguientes acciones:
 Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
 Retornar la cantidad total de reemplazos realizados.
'''
def reemplazar_nombres(lista_nombres:list,nombre_antiguo:str,nombre_nuevo:str)->list:
    """Reemplaza los nombres de una lista por uno actualizado.

    Args:
        lista_nombres (list): Lista de nombres.
        nombre_antiguo (str): Nombre a reemplazar.
        nombre_nuevo (str): Nombre de reemplazo.

    Returns:
        list: Lista con los nombres reemplazados.
    """
    cantidad_reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            cantidad_reemplazos += 1
    return cantidad_reemplazos

nombres = ["Juan","Priscila","Juan","Joaquin"]
#print(reemplazar_nombres(nombres,"Juan","Juanse"))
#print(nombres)

#9- Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la intersección de los dos arrays.
primeras_notas = [3,6,8,9,1,6]
segundas_notas = [6,2,7,9,10]
def interseccion_listas(lista1:list,lista2:list)->list:
    """Busca los elementos que se repiten en dos listas y los retorna en una lista.

    Args:
        lista1 (list): Primera lista a comparar.
        lista2 (list): Segunda lista a comparar.

    Returns:
        list: Elementos que se repiten.
    """
    interseccion = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista2[j] == lista1[i]:
                interseccion.append(lista2[j])

    return interseccion

#print(interseccion_listas(primeras_notas,segundas_notas))

def interseccion_2(lista1,lista2):
    diferencias = []
    for i in range(len(lista1)):
        diferente = True
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                diferente = False
        if diferente == False:
            diferencias.append(lista1[i])
    return diferencias

#print(interseccion_2(primeras_notas,segundas_notas))

def interseccion_listas_3(lista1, lista2):
    """Busca los elementos que se repiten en dos listas y los retorna en una lista.

    Args:
        lista1 (list): Primera lista a comparar.
        lista2 (list): Segunda lista a comparar.

    Returns:
        list: Elementos que se repiten.
    """
    interseccion = []
    for i in lista1:
        if i in lista2 and i not in interseccion:
            interseccion.append(i)
    return interseccion

#print(interseccion_listas_3(primeras_notas,segundas_notas))


#10- Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la unión de los dos arrays.
def union_listas(lista1:list,lista2:list)->list:
    """Realiza la union de los elementos de dos lista y los guarda en una nueva lista.

    Args:
        lista1 (list): Primera lista a comparar.
        lista2 (list): Segunda lista a comparar.

    Returns:
        list: Lista de la unificacion de las dos listas pasadas por parametro.
    """
    union = []
    todo = []
    flag = True
    for numero1 in range(len(lista1)):
        todo.append(lista1[numero1])
    for numero2 in range(len(lista2)):
        todo.append(lista2[numero2])
    for i in range(len(todo)):
        contador = 0
        if flag:
            union.append(todo[i])
            contador += 1
            flag = False
        else:
            for j in range(len(union)):
                if todo[i] == union[j]:
                    contador += 1
        if contador == 0:
            union.append(todo[i])

    return union

#print(union_listas(primeras_notas,segundas_notas))

#11- Crear una función que reciba como parámetros dos arrays. La función deberá retornar un array con la diferencia de los dos arrays.
def diferencias_lista(lista1:list,lista2:list)->list:
    """Retorna los de la primera lista pasada por parametro que son diferentes a la segunda lista pasada por parametro.

    Args:
        lista1 (list): Primera lista a comparar.
        lista2 (list): Segunda lista a comparar.

    Returns:
        list: Lista de elementos de la primera lista diferentes de la segunda lista.
    """
    diferencias = []
    for i in range(len(lista1)):
        diferente = True
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                diferente = False
        if diferente:
            diferencias.append(lista1[i])
    return diferencias

#print(diferencias_lista(segundas_notas,primeras_notas))
        