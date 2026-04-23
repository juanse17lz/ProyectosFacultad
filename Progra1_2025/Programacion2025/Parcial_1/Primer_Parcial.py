from Funciones.parcial_funciones import *

matriz_notas = [[4, 3, 7, 9, 6],
[5, 8, 4, 1, 8],
[2, 10, 3, 8, 7],
[2, 4, 5, 8, 4],
[3, 1, 4, 1, 2],
[4, 8, 4, 9, 1],
[7, 2, 10, 7, 7],
[10, 6, 7, 4, 10],
[5, 10, 8, 10, 6],
[10, 4, 7, 10, 5],
[4, 9, 9, 5, 10],
[5, 7, 9, 10, 1],
[10, 6, 4, 4, 1],
[6, 1, 10, 2, 10],
[8, 4, 5, 7, 8],
[4, 2, 7, 10, 3],
[2, 4, 1, 10, 4],
[8, 2, 6, 3, 7],
[5, 5, 7, 6, 6],
[2, 6, 4, 7, 1],
[3, 8, 3, 3, 2],
[8, 4, 7, 5, 6],
[3, 10, 9, 3, 3],
[6, 1, 10, 6, 8],
[5, 6, 3, 3, 3],
[10, 3, 5, 5, 8],
[2, 10, 1, 9, 7],
[10, 6, 3, 8, 7],
[2, 10, 6, 5, 3],
[3, 8, 9, 6, 1]]
alumnos = ['Pri', 'Andrea', 'Romina', 'Camila', 'Tita', 'Gra', 'Joa', 'Vicky', 'Valen', 'Juan',
 'Yamal', 'Kyle', 'Nati', 'Nico', 'Robin', 'Nami', 'Camie', 'Lali', 'Agus', 'Exe',
 'Julian', 'Juli', 'Martin', 'Emi', 'Emilia', 'Jesus', 'Fiama', 'Adrian', 'Barbie', 'Maxi']
generos = ['F', 'X', 'F', 'F', 'F', 'F', 'M', 'F', 'F', 'M',
 'X', 'F', 'F', 'M', 'F', 'X', 'X', 'X', 'F', 'M',
 'M', 'F', 'M', 'M', 'F', 'M', 'X', 'M', 'X', 'M']
legajos = ["50946", "48259", "25604", "88199", "15498", "97806", "26134", "57622", "82335", "80047",
 "54063", "49973", "21050", "99387", "38716", "63166", "49096", "92491", "72783", "95699",
 "32216", "89819", "39911", "72428", "91119", "37999", "71669", "75772", "55806", "67455"]

menu_opciones = "\nMENU DE OPCIONES\n\n1) Carga de Alumnos\n2) Mostrar datos.\n3) Calcular promedio de estudiantes. \n4) Ordenar de manera ascendente o descendente. \n5) Materias con mayor promedio general. \n6) Buscar por legajo.\n7) Mostrar repeticiones de notas de una materia.\n8) Salir del programa.\n"
mostrar_menu = "\nMOSTRAR\n\n1) Todos los datos.\n2) Lista de Alumnos.\n3) Todas las notas.\n4) Lista de generos.\n5) Lista de legajos.\n6) Lista de promedios.\n7) Volver.\n"
ingreso_menu = "\nIngreso de datos.\n\n1) Cargar datos de forma manual.\n2) Usar datos ya cargados. \n3) Volver al menu.\n"
ordenamiento_menu = "\nOrdenar los datos:\n1) Ascedente.\n2) Descendente.\n3) Volver al menu.\n"
elegir_materia = "\nIngrese la materia a visualizar las notas (1 al 5):\n"
mensaje_flags = "\nNo se puede ingresar sin haber cargado los datos primero."
menu_on = True
flag_ingreso_datos = False
flag_promedios = False

while menu_on:
    opcion = menu(menu_opciones)
    match opcion:
        case 1:
            ingreso = menu(ingreso_menu)
            match ingreso:
                case 1:
                    lista_alumnos = crear_array(3,"S")
                    lista_generos = crear_array(len(lista_alumnos),"S")
                    lista_legajos = crear_array(len(lista_alumnos),"S")
                    notas = inicializar_matriz(len(lista_alumnos),5,0)
                    cargar_datos_alumnos(notas,lista_alumnos,lista_generos,lista_legajos,"Ingrese la nota del alumno: ","Error, el dato ingresado es incorrecto. ",1,10,"Nombre del alumno: ","Error, vuela a ingresar el alumno: ","Ingrese un genero (F - Female / M - Male/ X- Sin Especificar): ","Error, vuelva a ingresar un genero (F - Female / M - Male/ X- Sin Especificar): ","Inserte un legajo de 5 digitos: ","Erros dato ingresado incorrecto.")
                    flag_ingreso_datos = True
                    flag_promedios = False
                case 2:
                    lista_alumnos = alumnos
                    lista_generos = generos
                    lista_legajos = legajos
                    notas = matriz_notas
                    print("\nUsando datos Hardcodeados.")
                    flag_ingreso_datos = True
                case 3:
                    print("\nVolviendo al menu.")
                case _:
                    print("\nOpcion invalida, volviendo al menu")
        case 2:
            if flag_ingreso_datos:
                mostrar = menu(mostrar_menu)
                match mostrar:
                    case 1:
                        if flag_promedios:
                            print("\nNOTAS\t\tALUMNOS\t\tGENEROS\t\tLEGAJOS\t\tPROMEDIOS\n")
                        else:
                            print("\nNOTAS\t\tALUMNOS\t\tGENEROS\t\tLEGAJOS\n")
                        for f in range(len(notas)):
                            for c in range(len(notas[0])):    
                                print(notas[f][c],end=" ")
                            print("\t",lista_alumnos[f],end="\t\t")
                            print(lista_generos[f],end="\t\t")
                            print(lista_legajos[f],end="\t\t")
                            if flag_promedios:
                                print(lista_promedios[f],end=" ")
                            print("")
                    case 2:
                        print("\nALUMNOS\n")
                        printear_lista(lista_alumnos)
                    case 3:
                        print("\nNOTAS\n")
                        printear_matriz(notas)
                    case 4:
                        print("\nGENEROS\n")
                        printear_lista(lista_generos)
                    case 5:
                        print("\nLEGAJOS\n")
                        printear_lista(lista_legajos)
                    case 6:
                        if flag_promedios:
                            print("\nPROMEDIOS\n")
                            printear_lista(lista_promedios)
                        else:
                            print("\nLa lista promedios aun no ha sido generada.")
                    case 7:
                        print("\nVolviendo al menu.")
                    case _:
                        print("\nOpcion invalida, volviendo al menu.")
            else:
                print(mensaje_flags)
        case 3:
            if flag_ingreso_datos:
                lista_promedios = promedios_filas_matriz(notas)
                flag_promedios = True
            else:
                print(mensaje_flags)
        case 4:
            if flag_ingreso_datos and flag_promedios:
                ordenar = menu(ordenamiento_menu)
                match ordenar:
                    case 1:
                        ordenar_datos_alumnos(lista_promedios,lista_alumnos,lista_generos,lista_legajos,notas)
                    case 2:
                        ordenar_datos_alumnos(lista_promedios,lista_alumnos,lista_generos,lista_legajos,notas,"desc")
                    case 3:
                        print("\nVolviendo al menu.")
                    case _:
                        print("\nOpcion invalida, volviendo al menu")
            else:
                print(mensaje_flags)
        case 5:
            if flag_ingreso_datos:
                lista_promedio_materias = promedios_columna_matriz(notas)
                maximos_elementos_lista(lista_promedio_materias,"Materia")
            else:
                print(mensaje_flags)
        case 6:
            if flag_ingreso_datos and flag_promedios:
                mostrar_por_legajo(lista_legajos,lista_promedios,lista_alumnos,lista_generos,notas,"\nIngresa el legajo a buscar: ","No se han encontrado coincidencias en la busqueda. ","\nNOTAS\t\tALUMNO\t\tGENERO\t\tLEGAJO\t\tPROMEDIO\n")
            else:
                print(mensaje_flags)
        case 7:
            if flag_ingreso_datos:
                materia = menu(elegir_materia)
                if materia > 0 and materia <= len(notas[0]):
                    repeticiones = repeticion_notas(notas,materia)
                    print(f"\nMateria_{materia}\n")
                    for i in range(len(repeticiones)):
                        print(f"Nota: {i+1} Repeticiones: {repeticiones[i]}")
                else:
                    print("\nLa materia solicitada no existe.")
            else:
                print(mensaje_flags)
        case 8:
            print("\nSaliendo del programa.")
            menu_on = False
        case _:
            print("\nOpcion invalida, vuelva a intentarlo.")
