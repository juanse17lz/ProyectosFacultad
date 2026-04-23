def palindromo(palabra:str)->bool:
    """Determina si una palabra es un palindromo o no.

    Args:
        palabra (str): Palabra a determinar.

    Returns:
        bool: "True" si es palindromo, "False" si no lo es.
    """
    es_palindromo = True
    for i in range(len(palabra)):
        if palabra[i] != palabra[len(palabra)-1-i]:
            es_palindromo = False
            break
    return es_palindromo

def unificar_frase(cadena:str)->str:
    """Elimina los espacios vacios de una cadena de caracteres.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        str: Cadena sin espacios vacios.
    """
    lista_cadena = ""
    for i in range(len(cadena)):
        if cadena[i] != " ":
            lista_cadena += cadena[i]
    return lista_cadena


def palindromo(palabra:str)->bool:
    Es_Palindromo=True
    for i in range(len(palabra)):   
        if palabra[i] != palabra[(len(palabra)-1)-i]:

            Es_Palindromo=False
            break
    return Es_Palindromo
def limpiar_espacios(palabra:str)->str:
    lista_frase=""
    for i in range(len(palabra)):
        if palabra[i] != " ":
            lista_frase+=palabra[i]
    return lista_frase
def inicializar_matriz(cant_filas, cant_columnas, valor_inicial):
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

palabras=["reconocer","luz azul","ojo","neuquen","pepe"]
matriz=inicializar_matriz(len(palabras),2,"")


for i in range(len(palabras)):
    palabra=palabras[i]
    palabras_sin_espacios=limpiar_espacios(palabra)
    es_palindromo=palindromo(palabras_sin_espacios)
    for j in range(len(matriz[i])):
        if j==0:
            matriz[i][j]=palabra
        else:
            matriz[i][j]=es_palindromo
mostrar_matriz(matriz)
