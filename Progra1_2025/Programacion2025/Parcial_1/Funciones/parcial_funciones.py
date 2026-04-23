def verificar_nombre(cadena:str)->bool:
    """Determina si en una cadena de caracteres alguno de sus digitos es un numero.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        bool: Devuelve True si contiene numeros, caso contrario devuelve False.
    """
    contiene_numero = False
    for i in cadena:
        if ord(i) >= 48 and ord(i) <= 57:
            contiene_numero = True
            break
    return contiene_numero

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

def printear_datos_matriz(matriz:list):
    """Recibe una matriz y muestra en pantalla todos sus elementos y su posicion en la matriz.

    Args: 
        matriz (list): Matriz a mostrar.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(f"Fila:{f} Columna:{c} Elemento: {matriz[f][c]}")

def printear_matriz(matriz:list):
    """Muestra en pantalla la matriz pasada por parametro.

    Args:
        matriz (list): Matriz a mostrar.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end= " ")
        print("")

def printear_lista(lista:list):
    """Recibe una lista y muestra sus elementos por pantalla.

    Args:
        lista (list): Lista cualquiera.
    """
    for i in range(len(lista)):
        print(lista[i])

def printear_fila_matriz(matriz:list,indice:int):
    """Recibe una matriz y un indice, y muestra los elementos de la fila por pantalla.

    Args:
        lista (list): Matriz cualquiera.
        indice (int): Indice de la fila a mostrar.
    """
    for c in range(len(matriz[indice])):
        print(matriz[indice][c],end=" ")

def inicializar_matriz(filas:int,columnas:int,valor_inicial=0)->list:
    """Inicializa una matriz con la cantidad de filas y columas ingresadas. Por defecto los elmentos seran ceros pero se le puede pasar por parametro el valor de los elementos iniciales. 

    Args:
        filas (int): Cantidad de filas que tendra la matriz.
        columnas (int): Cantida de columnas que tendra la matriz.
        valor_inicial : Valor inicial que tendran los elementos de la matriz, por defecto en cero.

    Returns:
        list: Retorna la matriz inicializada.
    """
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def crear_array(longitud:int,valor_inicial:str)->list:
    """Crea una lista de elementos vacios con la longitud del parametro ingresado.

    Args:
        longitud (int): Longitud de la lista.
        valor_inicial (str): Valor que tendran inicialmente los elementos de la lista.

    Returns:
        list: Lista de elementos vacios con la longitud ingresada.
    """
    lista = [valor_inicial] * longitud
    return lista


def buscar_en_matriz(matriz:list,dato:int):
    """Busca en la matriz el elemento pasado por parametro.

    Args:
        matriz (list): Matriz donde se realizara la busqueda.
        dato (int): Dato a buscar en la matriz.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] == dato:
                print(f"El dato {dato} se encuentra en la fila {f}, columna {c}.")

def insertar_datos_numericos_en_matriz(matriz:list, mensaje:str, mensaje_error:str, minimo:int, maximo:int,fila:str="Fila", columna:str="Columna"):
    """Valida y carga datos numericos en una matriz pasada por parametro.

    Args:
        matriz (list): Matriz a cargar.
        mensaje (str): Mensaje de solicitud de datos.
        mensaje_error (str): Mensaje de error por dato mal cargado.
        minimo (int): Valor mininmo a ingresar.
        maximo (int): Valor maximo a ingresar.
        fila (str): Mensaje que se mostrara para indicar la fila.
        columna (str): Mensaje que se mostrara para indicar la columna.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            dato_valido = False
            while dato_valido == False:
                print(f"{fila} {f+1} - {columna} {c+1}")
                dato = input(mensaje)
                validacion = validate_number(dato)
                if validacion:
                    numero = int(dato)
                    if numero >= minimo and numero <= maximo:
                        matriz[f][c] = numero
                        dato_valido = True
                    else:
                        print(mensaje_error)
                else:
                    print(mensaje_error)

def insertar_alumnos(cantidad_alumnos:int,mensaje:str,mensaje_error:str)->list:
    """Crea una lista de alumnos y valida que los datos ingresados sean numeros.

    Args:
        cantidad_alumnos (int): Cantidad de alumnos a ingresar.
        mensaje (str): Mensaje que se mostrara al pedir el nombre a ingresar.
        mensaje_error (str): Mensaje que se mostrara en caso de que el dato cargado sea incorrecto.

    Returns:
        list: Retorna la lista de alumnos.
    """
    alumnos = ["s"] * cantidad_alumnos
    for i in range(len(alumnos)): 
        nombre = input(mensaje)
        es_nombre = verificar_nombre(nombre)
        while es_nombre:
            nombre = input(mensaje_error)
            es_nombre = verificar_nombre(nombre)
        alumnos[i] = nombre
    return alumnos

def insertar_legajo(cantidad_legajos:int,mensaje:str,mensaje_error:str,largo_legajo:int)->list:
    """Crea una lista de legajos y valida que los datos ingresados no se repitan y que esten dentro del rango establecido.

    Args:
        cantidad_legajos (int): Cantidad de legajos a ingresar.
        mensaje (str): Mensaje que se mostrara para realizar la carga del legajo.
        mensaje_error (str): Mensaje que se mostrara en caso del que dato cargado sea incorrecto.
        largo_legajo (int): La longitud que debera tener cada legajo.

    Returns:
        list: Lista de lejagos
    """
    lista_legajos = [0] * cantidad_legajos
    for i in range(len(lista_legajos)):
        legajo_valido = False
        while legajo_valido != True:
            legajo = input(mensaje)
            es_numero = validate_number(legajo)
            if es_numero == True:
                numero = int(legajo)
                if len(legajo) == largo_legajo and numero > 0:
                    repetido = False
                    for l in range(len(lista_legajos)):
                        if legajo == lista_legajos[l]:
                            repetido = True
                            break
                    if repetido == False:
                        lista_legajos[i] = legajo
                        legajo_valido = True
                    else:
                        print(mensaje_error)
                else:
                    print(mensaje_error)
            else:
                print(mensaje_error)
    return lista_legajos

def insertar_generos(cantidad_generos:int,mensaje:str,mensaje_error:str,primer_parametros:str="F",segundo_parametro:str="M",tercer_parametros:str="X")->list:
    """Crea una lista de generos y valida los generos ingresados por parametro.

    Args:
        cantidad_generos (int): Cantidad de generos a ingresar.
        mensaje (str): Mensaje que mostrara para pedir los datos.
        mensaje_error (str): Mensaje que se mostrara para pedir los datos en caso de error.
        primer_parametros (str, optional): Parametro a comparar con los datos. Defaults to "F".
        segundo_parametro (str, optional): Parametro a comparar con los datos. Defaults to "M".
        tercer_parametros (str, optional): Parametro a comparar con los datos. Defaults to "X".

    Returns:
        list: Lista de Generos.
    """
    lista_generos = ["n/a"] * cantidad_generos
    for i in range(len(lista_generos)):
        genero = input(mensaje)
        while genero != primer_parametros and genero != segundo_parametro and genero != tercer_parametros:
            genero = input(mensaje_error)
        lista_generos[i] = genero
    return lista_generos

def promedios_lista(lista:list)->int:
    """Calcula el promedio una lista pasada por parametro.

    Args:
        lista (list): Lista a calcular promedio.

    Returns:
        int: Promedio de la lista.
    """
    acumulador = 0
    contador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
        contador +=1
    promedio = acumulador/contador
    return promedio

def promedios_filas_matriz(matriz:list)->list:
    """Recibe una matriz y devuelve una lista con el promedio de cada una de las filas de la matriz

    Args:
        matriz (list): Matriz numerica.

    Returns:
        list: Lista de promedios.
    """
    lista_promedios = [0] * len(matriz)
    for i in range(len(matriz)):
        lista_promedios[i] = promedios_lista(matriz[i])
    print("\nLos promedios se han calculado con exito.")
    return lista_promedios

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

def maximos_elementos_lista(lista:list,mensaje:str):
    """Imprime los elementos que tengan el valor maximo en la lista.

    Args:
        lista (list): Lista de elementos tipo "int".
        mensaje (str): Mensaje que mostrara el elemento que esta mostrando
    """
    maximo = maximo_lista(lista)
    for i in range(len(lista)):
        if lista[i] == maximo:
            print(f"{mensaje}_{i+1}: {lista[i]}")


def promedios_columna_matriz(matriz:list)->list:
    """Recibe una matriz y calcula el promedio de cada una de las columnas de la matriz.

    Args:
        matriz (list): Matriz a calcular promedio de sus columnas.

    Returns:
        list: Lista de promedios de columnas.
    """
    promedio_columnas = [0] * len(matriz[0])
    for c in range(len(matriz[0])):
        acumulador = 0
        contador = 0
        for f in range(len(matriz)):
            acumulador += matriz[f][c]
            contador += 1
        promedio = acumulador/contador
        promedio_columnas[c] = promedio
    return promedio_columnas

def buscar_por_legajo(lista_legajos:list,mensaje:str)->int|None:
    """Busca por legajo el indice del mismo.

    Args:
        lista_legajos (list): Lista donde se va a buscar el legajo.
        mensaje (str): Mensaje que pedira el dato a buscar.

    Returns:
        int|None: Devuelve el indice del legajo si es que lo encuentra.
    """
    indice = None
    legajo = input(mensaje)
    for i in range(len(lista_legajos)):
        if lista_legajos[i] == legajo:
            indice = i
            break
    return indice

def mostrar_por_legajo(lista_legajos:list,lista_promedios:list,lista_alumnos:list,lista_generos:list,notas:list,mensaje:str,mensaje_error:str,titulo:str):
    """Busca el legajo pasado por parametro y muestra los datos de asociados a ese legajo. 

    Args:
        lista_legajos (list): Lista de legajos.
        lista_promedios (list): Lista de promedios.
        lista_alumnos (list): Lista de alumnos.
        lista_generos (list): Lista de generos.
        notas (list): Matriz de notas.
        mensaje (str): Mensaje de busqueda.
        mensaje_error (str): Mensaje en caso de que la busqueda no se exitosa.
        titulo (str): Titulo de datos.
    """
    indice = buscar_por_legajo(lista_legajos,mensaje)
    if type(indice) == int:
        print(titulo)
        printear_fila_matriz(notas,indice)
        print("\t",lista_alumnos[indice],end=" ")
        print("\t\t",lista_generos[indice],end=" ")
        print("\t\t",lista_legajos[indice],end=" ")
        print("\t\t",lista_promedios[indice],end=" ")
        print("\n")
    else:
        print(mensaje_error)

def insertar_genero(lista_generos,indice,mensaje,mensaje_error,primer_parametro:str="F",segundo_parametro:str="M",tercer_parametro:str="X"):
    """Inserta el genero en la lista en el indice pasado por parametro, primero validad que el dato este bien ingresado.

    Args:
        lista_generos (_type_): Lista de generos.
        indice (_type_): Indice donde se va a cargar el dato.
        mensaje (_type_): Mensaje que pedira el dato a ingresar.
        mensaje_error (_type_): Mensaje que se mostrara en caso de que el dato cargado sea incorrecto.
        primer_parametro (str, optional): Primer parametro a validar el dato. Defaults to "F".
        segundo_parametro (str, optional): Segundo parametro a validar el dato. Defaults to "M".
        tercer_parametro (str, optional): Tercer parametro a validar el dato. Defaults to "X".
    """
    genero = input(mensaje)
    while genero != primer_parametro and genero != segundo_parametro and genero != tercer_parametro:
        genero = input(mensaje_error)
    lista_generos[indice] = genero

def insertar_legajo(lista_legajos:list,indice:int,mensaje:str,mensaje_error:str,largo_legajo:int):
    """Valida y carga el legajo en la lista de legajos en la posicion pasada por parametro.

    Args:
        lista_legajos (list): Lista de legajos.
        indice (int): Indice donde se cargara el legajo.
        mensaje (str): Mensaje que pedira el legajo a cargar.
        mensaje_error (str): Mensaje que se mostrara en caso de que el dato cargado sea incorrecto.
        largo_legajo (int): Longitud que debera tener el legajo cargado.
    """
    legajo_valido = False
    while legajo_valido != True:
        legajo = input(mensaje)
        es_numero = validate_number(legajo)
        if es_numero == True:
            numero = int(legajo)
            if len(legajo) == largo_legajo and numero > 0:
                repetido = False
                for l in range(len(lista_legajos)):
                    if legajo == lista_legajos[l]:
                        repetido = True
                        break
                if repetido == False:
                    lista_legajos[indice] = legajo
                    legajo_valido = True
                else:
                    print(mensaje_error)
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)

def insertar_alumno(lista_alumnos:list,indice:int,mensaje:str,mensaje_error:str):
    """Valida que se cargue un nombre de un alumno y lo guarda en una lista en la posicion pasada por parametro.

    Args:
        lista_alumnos (list): Lista donde se guardara el dato cargado.
        indice (int): Indice de la posicion donde se guardara el dato cargado en la lista.
        mensaje (str): Mensaje que pedira el dato a cargar.
        mensaje_error (str): Mensaje que se mostrara en caso de que le dato cargado sea incorrecto.
    """
    nombre = input(mensaje)
    es_nombre = verificar_nombre(nombre)
    while es_nombre:
        nombre = input(mensaje_error)
        es_nombre = verificar_nombre(nombre)
    lista_alumnos[indice] = nombre

def insertar_fila_de_notas(matriz_notas:list,indice:int,mensaje:str,mensaje_error:str,minimo:int,maximo:int,fila:str="Fila",columna:str="Columna"):
    """Recibe una matriz y un incide, y en la fila correspondiente al indice carga las notas del alumno, siempre validando que los datos sean correctos.

    Args:
        matriz_notas (list): Matriz de notas.
        indice (int): Indice de la fila donde se cargaran los datos.
        mensaje (str): Mensaje que pedira el dato a cargar.
        mensaje_error (str): Mensaje que se mostrara en caso de que el dato cargado sea incorrecto.
        minimo (int): Valor minimo que debera tener el dato a cargar.
        maximo (int): Valor maximo que debera tener el dato a cargar
        fila (str, optional): Mensaje que indicara la fila donde se esta cargando el dato. Defaults to "Fila".
        columna (str, optional): Mensaje que indicara la columna donde se esta cargando el dato. Defaults to "Columna".
    """
    for c in range(len(matriz_notas[indice])):
        dato_valido = False
        while dato_valido == False:
            print(f"{fila} {indice+1} - {columna} {c+1}")
            dato = input(mensaje)
            validacion = validate_number(dato)
            if validacion:
                numero = int(dato)
                if numero >= minimo and numero <= maximo:
                    matriz_notas[indice][c] = numero
                    dato_valido = True
                else:
                    print(mensaje_error)
            else:
                print(mensaje_error)

def cargar_datos_alumnos(matriz_notas:list,lista_alumnos:list,lista_generos:list,lista_legajos:list,mensaje_notas:str,mensaje_notas_error:str,minimo:int,maximo:int,mensaje_alumnos:str,mensaje_error_alumnos:str,mensaje_generos:str,mensaje_error_generos:str,mensaje_legajo:str,mensaje_error_legajos:str):
    """Carga los datos del alumno de forma ordenada, primero carga las notas del alumno, luego su nombre, genero y legajo.

    Args:
        matriz_notas (list): Matriz donde se cargaran las notas del alumno.
        lista_alumnos (list): Lista donde se cargaran los nombres del alumno.
        lista_generos (list): Lista donde se cargaran el genero del alumno.
        lista_legajos (list): Lista donde se cargaran el legajo del alumno:
        mensaje_notas (str): Mensaje que pedira el ingreso de las notas.
        mensaje_notas_error (str): Mensaje que se mostrara en caso notas mal cargadas.
        minimo (int): Maximo de la nota a cargar.
        maximo (int): Minimo de la nota a cargar.
        mensaje_alumnos (str): Mensaje que perdiar el nombre del alumno.
        mensaje_error_alumnos (str): Mensaje que se mostrara en caso de que el nombre este mal cargado.
        mensaje_generos (str): Mensaje que pedira el genero del alumno.
        mensaje_error_generos (str): Mensaje que se mostrara en caso de que el genero este mal cargado.
        mensaje_legajo (str): Mensaje que pedira el legajo del alumno.
        mensaje_error_legajos (str): Mensaje que se mostrara en caso de que el genero este mal cargado.
    """
    for f in range(len(matriz_notas)):
        insertar_fila_de_notas(matriz_notas,f,mensaje_notas,mensaje_notas_error,minimo,maximo,"Alumno","Materia")
        insertar_alumno(lista_alumnos,f,mensaje_alumnos,mensaje_error_alumnos)
        insertar_genero(lista_generos,f,mensaje_generos,mensaje_error_generos)
        insertar_legajo(lista_legajos,f,mensaje_legajo,mensaje_error_legajos,5)
        print("El alumno ha sido cargado con exito.\n")

def ordenar_datos_alumnos(lista_promedios:list,lista_alumnos:list,lista_generos:list,lista_legajos:list,matriz_notas:list,criterio:str="asc"):
    """Recibe una lista de elementos numericos y los ordena de manera ascendente o descendente. 

    Args:
        lista (list): Lista de numeros.
        criterio (str): Criterio por defecto en ascendente "asc", para descendente deber ser "desc".
    """
    for i in range(0,len(lista_promedios)-1,1):
        for j in range(i+1,len(lista_promedios),1):
            if (lista_promedios[i] > lista_promedios[j] and criterio == "asc") or (lista_promedios[i] < lista_promedios[j] and criterio == "desc"): 
                aux_promedios = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = aux_promedios

                aux_alumnos = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[j]
                lista_alumnos[j] = aux_alumnos

                aux_generos = lista_generos[i]
                lista_generos[i] = lista_generos[j]
                lista_generos[j] = aux_generos

                aux_legajos = lista_legajos[i]
                lista_legajos[i] = lista_legajos[j]
                lista_legajos[j] = aux_legajos

                notas_aux = matriz_notas[i]
                matriz_notas[i] = matriz_notas[j]
                matriz_notas[j] = notas_aux
    print("Datos ordenados con exito.")

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

def repeticion_notas(matriz:list,materia:int)->list:
    """Recibe una matriz de notas numericas del 1 al 10, y crea una lista con las repeticiones de cada una de las notas.

    Args:
        matriz (list): Matriz numerica.
        materia (int): Indice de la columna de la materia.

    Returns:
        list: Lista de repeticiones.
    """
    repeticiones = crear_array(10,0)
    for f in range(len(matriz)):
        if matriz[f][materia-1] == 1:
            repeticiones[0] +=1
        elif matriz[f][materia-1] == 2:
            repeticiones[1] += 1
        elif matriz[f][materia-1] == 3:
            repeticiones[2] += 1
        elif matriz[f][materia-1] == 4:
            repeticiones[3] += 1
        elif matriz[f][materia-1] == 5:
            repeticiones[4] += 1
        elif matriz[f][materia-1] == 6:
            repeticiones[5] += 1
        elif matriz[f][materia-1] == 7:
            repeticiones[6] += 1
        elif matriz[f][materia-1] == 8:
            repeticiones[7] += 1
        elif matriz[f][materia-1] == 9:
            repeticiones[8] += 1
        elif matriz[f][materia-1] == 10:
            repeticiones[9] += 1
    return repeticiones