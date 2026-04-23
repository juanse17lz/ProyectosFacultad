import json
from Canciones import playlist_lady_gaga 
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

def lectura_csv(ruta:str)->list:
    with open(ruta, "r") as archivo:
        matriz = []
        nombre_columnas = archivo.readline().strip().split(",")
        matriz.append(nombre_columnas)

        for linea in archivo:

            linea = linea.rstrip("\n")
            fila = []
            valores = linea.split(",")

            for valor in valores:

                if valor.isdigit():
                    fila.append(int(valor))
                else:
                    fila.append(valor)
            
            matriz.append(fila)
    
    return matriz

def escritura_csv(ruta:str,matriz:list):
    with open(ruta,"w") as archivo:
        for fila in  matriz:
            linea = ""
            for i in range(len(fila)):
                
                linea += str(fila[i])

                if i < (len(fila) - 1):
                    linea += ","
        
            archivo.write(linea + "\n")

def legibilizar_ruta(ruta:str)->str:
    nueva_ruta = ""
    aux = 0
    new = 0
    for i in range(len(ruta)):
        if ord(ruta[i]) == 92:
            new = i
            nueva_ruta += ruta[aux:new]
            aux = i+1
        if i == len(ruta):
            nueva_ruta += ruta[aux:i]
    return nueva_ruta

def llaves(diccionario:dict)->list:
    lista_llaves = []
    lista_llaves.append(diccionario.keys())
    return lista_llaves

#keys = llaves(playlist_lady_gaga[0])
#print(keys)

def formatiar_lista_diccionarios_a_csv(lista_diccionarios:list)->list:
    matriz = []
    line = []
    titulos = lista_diccionarios[0].keys()
    for titulo in titulos:
        line.append(titulo)
    matriz.append(line)

    for dicionario in lista_diccionarios:
        linea = []
        valores = dicionario.values()
        for valor in valores:
            linea.append(valor)
        matriz.append(linea)
    return matriz

def printear_matriz(matriz:list):
    """Muestra en pantalla la matriz pasada por parametro.

    Args:
        matriz (list): Matriz a mostrar.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end= " ")
        print("")

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
    vistas = int(visualizaciones[0:corte])
    return vistas

#print(convertir_visualizaciones_entereos("1300 millones"))

def colaboradores(colaboradores:str)->list:
    lista_colaboladores = ["S/N"]
    largo = len(colaboradores)
    for i in range(largo):
        if colaboradores[i] == "|":
            corte = i
            lista_colaboladores[0] = colaboradores[0:corte-1]
            lista_colaboladores.append(colaboradores[corte+2:largo])
            break
    return lista_colaboladores


def normalizar_datos_matriz(matriz:list):
    for f in range(len(matriz)-1):
        for c in range(len(matriz[0])):    
            if c == 1 and len(matriz[f+1][c]) > 0:
                matriz[f+1][c] = colaboradores(matriz[f+1][c])
            elif c == 2:
                matriz[f+1][c] = convertir_visualizaciones_entereos(matriz[f+1][c])
            elif c == 3:
                matriz[f+1][c] = convertir_minutero_segundo(matriz[f+1][c])
            elif c == 5:
                matriz[f+1][c] = date(matriz[f+1][c])
    matriz.remove(matriz[0])
    return matriz


"""canciones = formatiar_lista_diccionarios_a_csv(playlist_lady_gaga)
printear_matriz(canciones)
escritura_csv("Canciones.csv",canciones)"""


def promedios_vistas(matriz:list,indice:int)->list:
    acumulador = 0
    contador = 0
    for f in range(len(matriz)):
        acumulador += matriz[f][indice]
        contador += 1
    promedio = acumulador / contador
    return promedio


def listar_columna_matriz(matriz:list,indice:int)->list:
    lista = []
    for f in range(len(matriz)):
        lista.append(matriz[f][indice])
    return lista


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

def printear_lista_continua(lista:list):
    """Recibe una lista y muestra sus elementos por pantalla.

    Args:
        lista (list): Lista cualquiera.
    """
    for i in range(len(lista)):
        if type(lista[i]) == list:
            printear_lista_continua(lista[i])
        elif i == len(lista):
            print(lista[i])
        else:
            print(lista[i],end=" ")
            
def buscar_por_codigo(matriz:list,indice:int,codigo:str)->str|dict:
    retorno = "No se encontro el elemento buscado."
    for f in range(len(matriz)):
        if matriz[f][indice] == codigo:
            print("Encontrado con exito.")
            retorno = matriz[f]
            break
    return retorno

def formatear_lista_a_diccionario(formato_diccionario:dict,lista:list,keys:list)->list:
    for i in range(len(keys)):
        formato_diccionario[keys[i]] = lista[i]
    return formato_diccionario 

def formatear_matriz_a_lista_diccionarios(matriz:list,keys:list)->list:
    lista_diccionarios = []
    for f in range(len(matriz)):
        diccionario = formatear_lista_a_diccionario(matriz[f],keys)
        lista_diccionarios.append(diccionario)
    return lista_diccionarios

def lista_columna(matriz:list,indice:int)->list:
    columna = []
    for f in range(len(matriz)):
        columna.append(matriz[f][indice])
    return columna

def lista_fila(matriz:list,indice:int)->list:
    fila = []
    for c in range(len(matriz[0])):
        fila.append(matriz[indice][c])
    return fila

def escribir_json(lista_diccionarios:list,archivo:str):
    for i in range(len(lista_diccionarios)):
        with open(archivo, 'a') as archivo_json:
            json.dump(lista_diccionarios[i], archivo_json, indent=4)

def set_datos(lista:list)->set:
    retorno = set(lista)
    return retorno

def setear_colaboradores(matriz:list,indice:int)->set:
    for i in range(len(matriz)):
        if i == 0:
            seteo = set_datos(matriz[i][indice])
        else:
            seteo.update(matriz[i][indice])
    return seteo

def listar_colaboradores(matriz:list,indice:int):
    lista_colaboradores = []
    for f in range(len(matriz)):
        for a in matriz[f][indice]:
            if a not in lista_colaboradores:
                lista_colaboradores.append(a)
    return lista_colaboradores

def printear_lista(lista:set):
    """Recibe un set y muestra sus elementos y su indice por pantalla.

    Args:
        lista (list): Lista cualquiera.
    """
    for i in range(len(lista)):
        print(f"{i+1} - {lista[i]}")


def ordenar_matriz(matriz:list,indice:int,criterio:str="asc"):
    """Recibe una lista de elementos numericos y los ordena de manera ascendente o descendente. 

    Args:
        matriz (list): Matriz de numeros.
        criterio (str): Criterio por defecto en ascendente "asc", para descendente deber ser "desc".
    """
    for i in range(0,len(matriz)-1,1):
        for j in range(i+1,len(matriz),1):
            if (matriz[i][indice] > matriz[j][indice] and criterio == "asc") or (matriz[i][indice] < matriz[j][indice] and criterio == "desc"): 
                aux = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = aux

def date(fecha:str)->list:
    año_mes_dia = [0,0,0]
    mes = 0
    dia = 0
    for i in range(len(fecha)):
        if fecha[i] == "-" and mes == 0:
            mes = i
            año_mes_dia[0] = int(fecha[0:mes])
            mes += 1
        elif fecha[i] == "-" and mes != 0:
            dia = i
            año_mes_dia[1] = int(fecha[mes:dia])
            dia += 1
            año_mes_dia[2] = int(fecha[dia:len(fecha)])
    return año_mes_dia

"""
route = legibilizar_ruta("Programacion2025\Clases\Clase_13_Archivos\datos.csv")
print(route)
"""


    
