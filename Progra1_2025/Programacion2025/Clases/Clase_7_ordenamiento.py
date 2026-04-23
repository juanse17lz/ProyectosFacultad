numeros = [4,3,8,6,1,9,5,2,7]


def ordenar_array_asc(lista:list):
    """Recibe una lista de elementos numericos y los ordena de manera ascendente.

    Args:
        lista (list): Lista de numeros.
    """
    for i in range(0,len(lista)-1,1):
        for j in range(i+1,len(lista),1):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_array_desc(lista:list):
    """Recibe una lista de elementos numericos y los ordena de manera descendiente.

    Args:
        lista (list): Lista de numeros.
    """
    for i in range(0,len(lista)-1,1):
        for j in range(i+1,len(lista),1):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_array(lista:list,criterio:str="asc"):
    """Recibe una lista de elementos numericos y los ordena de manera ascendente o descendente. 

    Args:
        lista (list): Lista de numeros.
        criterio (str): Criterio por defecto en ascendente "asc", para descendente deber ser "desc".
    """
    for i in range(0,len(lista)-1,1):
        for j in range(i+1,len(lista),1):
            if (lista[i] > lista[j] and criterio == "asc") or (lista[i] < lista[j] and criterio == "desc"): 
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def copiar_array(lista:list)->list:
    """Recibe un lista y guarda una copia en una nueva variable.

    Args:
        lista (list): Lista a copiar.

    Returns:
        list: Copia de la lista original.
    """
    lista_guardada = []
    for i in range(len(lista)):
        lista_guardada.append(lista[i])
    return lista_guardada

def copiar_array_2(lista:list)->list:
    """Recibe un lista y guarda una copia en una nueva variable.

    Args:
        lista (list): Lista a copiar.

    Returns:
        list: Copia de la lista original.
    """
    lista_guardada = [-1] * len(lista)
    for i in range(len(lista)):
        lista_guardada[i] = lista[i]
    return lista_guardada

print(numeros)
ordenar_array(numeros,"asc")
print(numeros)
ordenar_array(numeros,"desc")
print(numeros)