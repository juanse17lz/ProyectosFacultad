def menu(menu_opciones:str)->int:
    """Recibe una cadena de caracteres y lo muestra por pantalla, luego pide ingresar una opcion y valida que la opcion ingresada sea numerica y la retorna.

    Args:
        menu_opciones (str): Cadena de caracteres o menu de opciones.

    Returns:
        int: Opcion elegida.
    """
    print(menu_opciones)
    opcion_valida = False
    while opcion_valida != True:
        opcion = input("Ingrese una opcion: ")
        if validate_number(opcion) == True:
            opcion = int(opcion)
            opcion_valida = True
    return opcion

def printear_lista_continua(lista:list):
    """Recibe una lista y muestra sus elementos por pantalla.

    Args:
        lista (list): Lista cualquiera.
    """
    for i in range(len(lista)):
        if i == len(lista):
            print(lista[i])
        else:
            print(lista[i],end=" ")


def validate_number(cadena:str)->bool:
    """Valida que los elementos de la cadena sean de caracter numerico.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        bool: True en caso de ser datos numericos, caso contrario el retorno sera False.
    """
    flag = False
    for i in cadena:
        if cadena == "":
            flag = False
        else:
            if ord(i) > 47 and ord(i) < 58:
                flag = True
            else:
                flag = False
                break
    return flag

def menu(menu_opciones:str)->int:
    """Recibe una cadena de caracteres y lo muestra por pantalla, luego pide ingresar una opcion y valida que la opcion ingresada sea numerica y la retorna.

    Args:
        menu_opciones (str): Cadena de caracteres o menu de opciones.

    Returns:
        int: Opcion elegida.
    """
    print(menu_opciones)
    opcion_valida = False
    while opcion_valida != True:
        opcion = input("Ingrese una opcion: ")
        if validate_number(opcion) == True:
            opcion = int(opcion)
            opcion_valida = True
    return opcion

def titulo(str)->str:
    titulo = ["s"] * len(str)
    for i in range(len(str)):
        if i == 0:
            titulo[i] = str[i].upper
        else:
            titulo[i] = str[i].lower
    return titulo

def llaves(diccionario:dict)->list:
    lista_llaves = []
    for x in diccionario:
        lista_llaves.append(x)
    return lista_llaves


def convertir_minutero_segundo(tiempo:str)->int:
    """Convierte el tiempo de duracion de un video en segundos:

    Args:
        str (str): Tiempo de duracion de un video

    Returns:
        int: Segundo que dura el video.
    """
    largo = len(tiempo)
    for i in range(largo):
        if tiempo[i] == ":":
            corte = i
            break
    mintuos = int(tiempo[0:corte]) * 60
    segundos = mintuos + int(tiempo[corte+1:largo])
    return segundos

#print(convertir_minutero_segundo("3:50"))

def convertir_visualizaciones_entereos(visualizaciones:str)->int:
    largo = len(visualizaciones)
    for i in range(largo):
        if visualizaciones[i] == " ":
            corte = i
            break
    vistas = int(visualizaciones[0:corte]) * 1000000
    return vistas

#print(convertir_visualizaciones_entereos("1300 millones"))

def colaboradores(colaboradores:str)->list:
    lista_colaboladores = []
    largo = len(colaboradores)
    for i in range(largo):
        if colaboradores[i] == "|":
            corte = i
    lista_colaboladores.append(colaboradores[0:corte-1])
    lista_colaboladores.append(colaboradores[corte+2:largo])
    return lista_colaboladores

#print(colaboradores("Juanse | Joaquin"))

"""def formatear_fecha(fecha:str):
    largo = len(fecha)
    for i in range(largo):
        if fecha[i] == "-":
            fecha[i] = "/"

dia = "2009-03-17"
formatear_fecha(dia)
print(dia)"""

def mostrar_diccionario(diccionario:dict,llaves:list):
    for i in range(len(diccionario)):
        if llaves[i] == "Colaboradores":
            print(f"{llaves[i]} : ",end="")
            printear_lista_continua(diccionario[llaves[i]])
            print("")
        else:
            print(f"{llaves[i]} : {diccionario[llaves[i]]}")


def normalizar_datos(diccionario:dict,llaves:list):
    for llave in llaves:
        if llave == "Colaboradores" and len(diccionario[llave]) > 0:
            diccionario[llave] = colaboradores(diccionario[llave])
        elif llave == "Vistas":
            diccionario[llave] = convertir_visualizaciones_entereos(diccionario[llave])
        elif llave == "Duracion":
            diccionario[llave] = convertir_minutero_segundo(diccionario[llave])

def listar_elemento_diccionario(lista_diccionarios:list,llave:str)->list:
    lista = []
    for diccionario in lista_diccionarios:
        lista.append(diccionario[llave])
    return lista

def promedios_vistas(lista_diccionarios:list,llave:str)->list:
    acumulador = 0
    contador = 0
    for diccionario in lista_diccionarios:
        acumulador += diccionario[llave]
        contador += 1
    promedio = acumulador / contador
    return promedio

def max_min_lista(lista:list,condicion:str="max")->int:
    """Busca y retorna el elmento con mayor o menor valor de una lista. Condiciones "max" o "min".

    Args:
        lista (list): Lista de elementos tipo "int".
        condindicion (str): Evalua que si se calcular el maximo o el mininimo. Defaults to "max".

    Returns:
        int: Elemento de maximo o minimo valor de la lista.
    """
    flag = False
    retorno = None
    for i in range(len(lista)):
        if flag == False:
            retorno = lista[i]
            flag = True 
        else:
            if (lista[i] > retorno and condicion == "max") or (lista[i] < retorno and condicion == "min"):
                retorno = lista[i]
    return retorno

def max_min_elementos_lista(lista:list,mensaje:str,condicion:str):
    """Imprime los elementos que tengan el valor maximo en la lista.

    Args:
        lista (list): Lista de elementos tipo "int".
        mensaje (str): Mensaje que mostrara el elemento que esta mostrando
    """
    parametro = max_min_lista(lista,condicion)
    for i in range(len(lista)):
        if lista[i] == parametro:
            print(f"{mensaje}_{i+1}: {lista[i]}")

def printear_lista(lista:list,titulo:str="TITULO"):
    """Recibe una lista y muestra sus elementos por pantalla.

    Args:
        lista (list): Lista cualquiera.
        titulo (str): Mostrara como titulo de la lista.
    """
    print(titulo)
    for i in range(len(lista)):
        print(f"{i+1}: {lista[i]}")

def ordenar_diccioniario(lista_diccionarios:list,llave:str):
    largo = len(lista_diccionarios)
    for i in range(largo):
        if i+1 == largo:
            break
        else:   
            if lista_diccionarios[i][llave] > lista_diccionarios[i+1][llave]:
                aux = lista_diccionarios[i]
                lista_diccionarios[i] = lista_diccionarios[i+1]
                lista_diccionarios[i+1] = aux
    print("Ordenamiento exitoso.")

def buscar_por_codigo(lista_diccionario:list,llave:str,codigo:str)->str|dict:
    retorno = "No se encontro el elemento buscado."
    for diccionario in lista_diccionario:
        if diccionario[llave] == codigo:
            print("Encontrado con exito.")
            retorno = diccionario
            break
    return retorno

def set_datos(lista:list)->set:
    retorno = set(lista)
    return retorno

def setear_colaboradores(lista_diccionario:list,llave:str):
    for i in range(len(lista_diccionario)):
        if i == 0:
            seteo = set_datos(lista_diccionario[i][llave])
        else:
            seteo.update(lista_diccionario[i][llave])
    return seteo
            
dicionario = {
        "Tema": "Just Dance",
        "Colaboradores" : "Colby O'Donis | Akon",
        "Vistas": "300 millones",
        "Duracion": "4:01",
        "Link Youtube": "https://www.youtube.com/watch?v=2Abk1jAONjw",
        "Fecha lanzamiento": "2008-04-08",
        "Key" : "0028"
    }

#lista = llaves(dicionario)
#normalizar_datos(dicionario,lista)
#print(dicionario)
"""
set = {"1"}
#set.update("1")
set_2 = ["1","2"]
print(type(set))
set.update(set_2)
print(type(set))
print(set)

datos = ["Charly","Duki"]
seteo = set_datos(datos)
print(type(seteo))
print(seteo)
"""