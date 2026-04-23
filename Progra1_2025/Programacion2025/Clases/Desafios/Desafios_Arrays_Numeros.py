from paquetes.arrays_funciones import *
from paquetes.funciones_especificas import *

'''
📌 Desafío: Menú de Opciones con Listas y Funciones
Desarrollar un programa en Python que presente un menú de opciones donde el usuario pueda realizar distintas operaciones con un conjunto de números.

🔹 Opciones del Menú:
 1️⃣ Ingresar datos: Permitir al usuario ingresar 10 números enteros en el rango de -1000 a 1000.
 2️⃣ Cantidad de positivos y negativos: Mostrar cuántos números ingresados son positivos y cuántos son negativos.
 3️⃣ Suma de los números pares: Calcular y mostrar la sumatoria de los números pares.
 4️⃣ Mayor número impar: Identificar y mostrar el mayor número impar ingresado.
 5️⃣ Listar los números ingresados: Mostrar todos los números en el orden en que fueron ingresados.
 6️⃣ Listar los números pares: Mostrar únicamente los números pares de la lista.
 7️⃣ Listar los números en posiciones impares: Mostrar los números que se encuentran en posiciones impares dentro de la lista.
 8️⃣ Salir del programa.

🔹 Condiciones:
 ✔️ El usuario debe ingresar los números antes de acceder a las opciones 2 a 7.
 ✔️ El programa debe estar estructurado en funciones, siguiendo el paradigma de programación funcional:
Funciones específicas: Para operaciones como determinar si un número es positivo, negativo o par.
Funciones generales: Para listar elementos o calcular sumatorias.

🔹 Estructura del Código:
 📌 El programa debe estar organizado en módulos:
Especificas.py: Contendrá las funciones específicas.
Array_Generales.py: Contendrá las funciones generales.

Las funciones de entrada de datos deben importarse desde el módulo Input.

🔹 Consejo:
 ✅ Desarrollar y probar primero cada función individualmente antes de organizarlas en módulos y paquetes.
'''


menu = True

menu_opciones = "\nMENU DE OPCIONES\n\n1_ Ingresar 10 datos numericos.\n2_ Cantidad de numeros negativos y positivos.\n3_ Suma de numeros pares.\n4_ Mostrar mayor numero impar.\n5_ Listar numeros ingresados.\n6_ Listar numeros pares.\7_ Listar numeros en posciones impares.\n8_ Salir del programa.\n\nIngrese su opcion: "

while menu:
    opcion = input(menu_opciones)
    match opcion:
        case "1":
            numeros = crear_array_numeros_validados(10,"Ingres 10 numeros entre -1000 y 1000.","Error. Dato incorrecto vuelva a ingresar un numero",-1000,1000)
            print(numeros)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            print("Saliendos del Programa")
            menu = False
        case _:
            pass
