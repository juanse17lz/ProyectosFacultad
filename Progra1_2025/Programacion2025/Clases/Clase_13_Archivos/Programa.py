import json
from funciones_archivos import *
from Canciones import playlist_lady_gaga

"""
canciones = formatiar_lista_diccionarios_a_csv(playlist_lady_gaga)
print(canciones)
escritura_csv("Canciones.csv",canciones)
"""
mensaje_menu = "MENU DE OPCIONES\n\n1) Normalizar datos\n2) Mostrar lista de temas\n3) Ordenar de mas a menos vistas\n4) Promedio de vistas\n5) Maxima reproducciones\n6) Minima reproducciones\n7) Buscar por codigo\n8) Listar por colaborador\n9) Listar por mes\n10) Guardar en .json\n11) Salir del programa\n"
programa = True
caso_1 = False

while programa:
    canciones = lectura_csv("Canciones.csv")
    opcion = menu(mensaje_menu)
    match opcion:
        case 1:
            normalizadas = normalizar_datos_matriz(canciones)
            print("Datos normalizados con exito.")
            caso_1 = True
        case 2:
            if caso_1:
                print("CANCIONES\n")
                for f in range(len(normalizadas)):
                    print(f"{f+1}: {normalizadas[f][0]}")
            else:
                print("Primero debe acceder a la opcion 1.")
        case 3:
            if caso_1:
                ordenar_matriz(normalizadas,3,"desc")
                print("Canciones oredenadas correctamenete:")
            else:
                print("Primero debe acceder a la opcion 1.")
        case 4:
            if caso_1:
                print("PROMEDIO\n")
                promedio = promedios_vistas(normalizadas,2)
                print(f"El promedio de las visualizaciones de los temas de Ladygaga es de {promedio} millones de {canciones[0][2]}.")
            else:
                print("Primero debe acceder a la opcion 1.")
        case 5:
            if caso_1:
                reproducciones = listar_columna_matriz(normalizadas,2)
                maximo = max_min_lista(reproducciones)
                for f in range(len(normalizadas)):
                    if normalizadas[f][2] == maximo:
                        print(f"{f+1}: ",end="")
                        printear_lista_continua(normalizadas[f])
                        print("\n")
            else:
                print("Primero debe acceder a la opcion 1.")            
        case 6:
            if caso_1:    
                reproducciones = listar_columna_matriz(normalizadas,2)
                minimo = max_min_lista(reproducciones,"min")
                for f in range(len(normalizadas)):
                    if normalizadas[f][2] == minimo:
                        print(f"{f+1}: ",end="")
                        printear_lista_continua(normalizadas[f])
                        print("\n")
            else:
                print("Primero debe acceder a la opcion 1.")
        case 7:
            if caso_1:
                codigo = input("Ingrese el codigo de la cancion: ")
                cancion = buscar_por_codigo(normalizadas,2,codigo)
                if type(cancion) == list:
                    printear_lista_continua(cancion)
                else:
                    print(cancion)
            else:
                print("Primero debe acceder a la opcion 1.")
        case 8:
            if caso_1:
                print("COLABORADORES\n\nLista de colaboradores:")
                mensaje = "No se han encontrado colaboradores"
                lista_coloaboradores = listar_colaboradores(normalizadas,1)
                printear_lista(lista_coloaboradores)
                opcion = menu("")
                for i in range(len(normalizadas)):
                    if lista_coloaboradores[opcion - 1] in normalizadas[i][1]:
                        print(f"{i+1} - ",end="")
                        printear_lista_continua(normalizadas[i])
                        print("\n")
                        mensaje = "Se mostraron todas las canciones donde participa el colaborador."
                print(mensaje)
            else:
                print("Primero debe acceder a la opcion 1.")
        case 9:
            if caso_1:
                opcion = menu("Elija de forma numerica un mes del año y se mostraran las canciones que hayan salido en ese mes.")
                for f in normalizadas:
                    if opcion in (f[5])[1]:
                        printear_lista_continua(f)
                        print("\n")
            else:
                print("Primero debe acceder a la opcion 1.")
        case 10:
            if caso_1:
                keys = lista_fila(canciones,0)
                lista_diccionarios = formatear_matriz_a_lista_diccionarios(normalizadas,keys)
                escribir_json(lista_diccionarios,"Canciones_LadyGaga.json")
                print("Datos guardados con exito.")
            else:
                print("Primero debe acceder a la opcion 1.")
        case 11:
            print("Saliendo del prgrama.")
            programa = False
        case _:
            print("Opcion invalida.")
