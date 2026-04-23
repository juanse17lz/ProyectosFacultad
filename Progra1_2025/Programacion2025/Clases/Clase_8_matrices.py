
def printear_datos_matriz(matriz:list):
    """Recibe una matriz y muestra en pantalla todos sus elementos y su posicion en la matriz.

    Args: 
        matriz (list): Matriz a mostrar.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(f"Fila:{f} Columna:{c} Elemento: {matriz[f][c]}")

def printear_matriz(matriz:list):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end= " ")
        print("")

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

#matrix = inicializar_matriz(2,4,"S")
#printear_datos_matriz(matrix)
matriz = [[2,5,7,9],
          [1,3,4,8]]
#uscar_en_matriz(matriz,4)

def inicializar_matriz_cuadrada(tamaño:int,valor_inicial)->list:
    """Genera una matriz cuadrada, de misma cantidad de filas que de columnas, y la inicializa en un valor determinado.

    Args:
        tamaño (_type_): Tamaño de la matriz, cantidad de filas y de columnas.
        valor_inicial (_type_): Valor inical de los elementos de la matriz.

    Returns:
        list: Matriz cuadrada.
    """
    matriz = []
    for i in range(tamaño):
        fila = [valor_inicial] * tamaño
        matriz += [fila]
    return matriz

#nueva_matriz = inicializar_matriz_cuadrada(5,0)
#print(nueva_matriz)

def crear_matriz_simetrica(matriz:list,elemento_inicial:int):
    """Crea una matriz simetrica, a partir de un elemento inicial.

    Args:
        matriz (list): Matriz inicializada.
        elemento_inicial (int): Valor del elemento inicial.
    """
    if len(matriz) == len(matriz[0]):
        for f in range(len(matriz)):
            for c in range(len(matriz[f])):
                if f == c:
                    matriz[f][c] = elemento_inicial
                else:
                    matriz[f][c] = (elemento_inicial+f) + (elemento_inicial+c)
    else:
        print("La matriz no es cuadrada.")

#crear_matriz_simetrica(matriz,1)
#printear_matriz(nueva_matriz)

def calcular_constante_magica(matriz:list)->int:
    """Calcula la constante de magica de una matriz magica.

    Args:
        matriz (list): Matriz magica.

    Returns:
        int: Valor de la constante magica.
    """
    constante_magica = (len(matriz)*(len(matriz)*len(matriz)+1))/2
    return constante_magica

def determinar_matriz_magica(matriz:list)->bool:
    """Determina si una matriz es magica o no.

    Args:
        matriz (list): Recibe una matriz cualquiera.

    Returns:
        bool: En caso de ser magica retorna "True", caso contrario retornara "False".
    """
    es_magica = False
    if len(matriz) != len(matriz[0]):
        print("La matriz no es cuadrada.")
    else:
        constante_magica = calcular_constante_magica(matriz)
        acumulador_d = 0
        for f in range(len(matriz)):
            acumulador_f = 0
            acumulador_c = 0
            for c in range(len(matriz[f])):
                acumulador_f += matriz[f][c]
                acumulador_c += matriz[c][f]
                if f == c:
                    acumulador_d += matriz[f][c]
            if acumulador_c != constante_magica or acumulador_f != constante_magica:
                break
        if acumulador_d == constante_magica:
            es_magica = True
    return es_magica

'''
determinar_matriz_magica(matriz)
matriz_magica = [[16,2,3,13],
                 [5,11,10,8],
                 [9,7,6,12],
                 [4,14,15,1]] 
matriz_no_magica = [[1,2,3,10],
                    [4,5,6,11],
                    [7,8,9,12],
                    [13,14,15,16]]   
print(determinar_matriz_magica(matriz_magica))
print(determinar_matriz_magica(matriz_no_magica))
'''    

def copiar_matriz(matriz:list)->list:
    copia = inicializar_matriz(len(matriz),len(matriz[0]),0)

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            copia[f][c] = matriz[f][c]
    return copia

matriz1 = [[4,0],[1,-9],[1,-9]]
matriz2 = [[3,8,2],[4,6,4]]

#copiada = copiar_matriz(matriz1)
#printear_matriz(matriz1)
#printear_matriz(copiada)

def sumar_matrices(primera_matriz:list, segunda_matriz:list)->list|None:
    """Siempre que se pueda se realizara la suma de 2 matrices.

    Args:
        primera_matriz (list): Matriz a sumar.
        segunda_matriz (list): Matriz sumadora.

    Returns:
        list|None: Suma de matrices o "None".
    """
    if len(primera_matriz) != len(segunda_matriz) or len(primera_matriz[0]) != len(segunda_matriz[0]):
        matriz_resultante = copiar_matriz(primera_matriz)
        for f in range(len(primera_matriz)):
            for c in range(len(primera_matriz[f])):
                matriz_resultante[f][c] += segunda_matriz[f][c]
    else:
        print("La matriz no se puede sumar.")
        matriz_resultante = None
    return matriz_resultante

#print(sumar_matrices(matriz1,matriz2))

def escalar_matriz(matriz:list,escalar:int)->list:
    """Multiplica una matriz por el escalar.

    Args:
        matriz (list): Matriz.
        escalar (int): Escalar.

    Returns:
        list: Matriz escalada.
    """
    matriz_resultante = copiar_matriz(matriz)

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            matriz_resultante[f][c] = matriz[f][c] * escalar
    
    return matriz_resultante

#print(escalar_matriz(matriz1,2))

def multiplicar_matrices(primera_matriz:list,segunda_matriz:list)->list|None:
    """Siempre y cuando se pueda, la funcion realizara la multiplicacion de 2 matrices.

    Args:
        primera_matriz (list): Primera matriz.
        segunda_matriz (list): Segunda matriz.

    Returns:
        list|None: Matriz multiplicada. "None" si no se pueden multiplicar.
    """
    if len(primera_matriz[0]) == len(segunda_matriz):
        matriz_resultante = inicializar_matriz(len(primera_matriz),len(segunda_matriz[0]),0)
        for f in range(len(matriz_resultante)):
            for c in range(len(matriz_resultante[0])):
                for k in range(len(primera_matriz[0])):
                    matriz_resultante [f][c] += primera_matriz[f][k] * segunda_matriz[k][c]
    else:
        print("La matirz no se puede multiplicar")
        matriz_resultante = None

    return matriz_resultante

multiplicada = multiplicar_matrices(matriz1,matriz2)
printear_matriz(multiplicada)