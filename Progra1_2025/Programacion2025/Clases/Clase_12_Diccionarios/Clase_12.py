from Datos import playlist_lady_gaga 
from Funciones_ladygaga import *


mensaje_menu = "MENU DE OPCIONES\n\n1) Normalizar datos.\n2) Mostrar lista de temas.\n3) Ordenar temas.\n4) Promedio de Visitas.\n5) Maxima Reproduccio.\n6) Minima Reproduccion.\n7) Busqueda por codigo.\n8) Buscar por colaborador.\n9) Mes de lanzamiento.\n10) Salir.\n"
programa = True
caso_1 = False

while programa:
    opcion = menu(mensaje_menu)
    match opcion:
        case 1:
            lista_llaves = llaves(playlist_lady_gaga[0])
            for cancion in playlist_lady_gaga:
                normalizar_datos(cancion,lista_llaves)
            caso_1 = True
        case 2:
            if caso_1:
                lista_temas = listar_elemento_diccionario(playlist_lady_gaga,"Tema")
                printear_lista(lista_temas,"CANCIONES")
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 3:
            if caso_1:
                ordenar_diccioniario(playlist_lady_gaga,"Duracion")
                print("Se han ordenado los temas con exito.")
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 4:
            if caso_1:
                promedio = promedios_vistas(playlist_lady_gaga,"Vistas")
                print(f"El promedio de las vistas de Ladygaga es de: {promedio} de reproducciones.")
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 5:
            if caso_1:
                lista_reproduciones = listar_elemento_diccionario(playlist_lady_gaga,"Vistas")
                maximo = max_min_lista(lista_reproduciones)
                for i in range(len(lista_reproduciones)):
                    if lista_reproduciones[i] == maximo:
                        mostrar_diccionario(playlist_lady_gaga[i],lista_llaves)
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 6:
            if caso_1:
                lista_reproduciones = listar_elemento_diccionario(playlist_lady_gaga,"Vistas")
                minimo = max_min_lista(lista_reproduciones,"min")
                for i in range(len(lista_reproduciones)):
                    if lista_reproduciones[i] == minimo:
                        mostrar_diccionario(playlist_lady_gaga[i],lista_llaves)
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 7:
            if caso_1:
                codigo = input("Ingrese el codigo de la cancion: ")
                cancion = buscar_por_codigo(playlist_lady_gaga,"Key",codigo)
                if type(cancion) == dict:
                    mostrar_diccionario(cancion,lista_llaves)
                else:
                    print(cancion)
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 8:
            if caso_1:
                set_colaboradores = setear_colaboradores(playlist_lady_gaga,"Colaboradores")
                print(set_colaboradores)
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 9:
            if caso_1:
                pass
            else:
                print("Primero debe ingresar a la opcion 1.\n")
        case 10:
            print("Saliendo del Programa")
            programa = False
        case _:
            print("Opcion Invalida.\n")