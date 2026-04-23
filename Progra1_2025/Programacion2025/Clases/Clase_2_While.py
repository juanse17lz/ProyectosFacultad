'''
ejemplo = 0
suma = 1

while ejemplo < 10:
    ejemplo = ejemplo + suma
    print(ejemplo)
    if ejemplo >= 10:
        print("Fin")
'''

'''
#PORCENTAJES

no_valida = 0
encuesta = 0
pes = 0
fifa = 0
while encuesta < 15:
    respuesta = input("Que prefieres fifa o pes?")
    encuesta += 1
    match respuesta:
        case "fifa":
            fifa += 1
        case "pes":
            pes += 1
        case _:
            no_valida += 1
            print("Respuesta incorrecta")
            encuesta -= 1

porcentaje_fifa = (fifa * 100) / encuesta
porcentaje_pes = (pes * 100) / encuesta

print(f"El {porcentaje_fifa}% de personas juega Fifa.")
print(f"El {porcentaje_pes}% de personas juega Pes.")
'''

'''
#PROMEDIOS

notas = 0
alumnos = 0

while alumnos < 10:
    nota = input("Ingrese una nota: ")
    notas += int(nota)
    alumnos += 1

print(f"El promedio de notas de 10 alumnos es: {notas/alumnos}") 
'''

'''
#VALIDACION 

clave = int(input("ingrese su clave: "))
errores = 0
while clave != 619:
    if errores >= 2:
        print("Demasiados errores.")
        break
    errores += 1
    clave = int(input("Error. Ingrese su clave: "))
'''

'''
#EJERCICIOS
#1) Mostrar 10 repeticiones de números ascendentes desde el 1 al 10

numeros = 1
while numeros <= 10:
    print(numeros)
    numeros += 1
'''

'''
#2) Mostrar 10 repeticiones de números descendentes desde el 10 al 1

numeros = 10
while numeros >= 1:
    print(numeros)
    numeros -= 1
'''

'''
#3) Mostrar la suma de los números desde el 1 hasta el 10.

numeros = 1
acumulador = 0

while numeros <= 10:
    acumulador += numeros
    print(numeros)
    numeros += 1
print(acumulador)
'''

'''
#4) Mostrar la suma de los números pares desde el 1 hasta el 10.

numeros = 1
acumulador = 0

while numeros <= 10:
    if numeros % 2 == 0:
        acumulador += numeros
    print(numeros)
    numeros += 1
print(acumulador)
'''

'''
#5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

cantidad_numeros = 0
suma_numeros = 0

numero = int(input("Ingrese un numero: "))
cantidad_numeros += 1
suma_numeros += numero
while cantidad_numeros < 5:
    numero = int(input("Ingrese otro numero: "))
    cantidad_numeros += 1
    suma_numeros += numero

promedio = suma_numeros / cantidad_numeros

print(f"El promedio de los {cantidad_numeros} numeros ingresados es de: {promedio}")
'''

'''
#6) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

cantidad_numeros = 0
suma_numeros = 0

numero = int(input("Ingrese un numero o ingrese 0 para salir: "))
while numero != 0:
    cantidad_numeros += 1
    suma_numeros += numero
    numero = int(input("Ingrese otro numero o ingrese 0 para salir: "))

promedio = suma_numeros / cantidad_numeros

#print(cantidad_numeros)
#print(suma_numeros)

print(f"El promedio de los {cantidad_numeros} numeros ingresados es de: {promedio}")
'''

'''
#7) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

cantidad_numeros = 0
suma_positivos = 0
negativos = 0

numero = int(input("Ingrese un numero o ingrese 0 para salir: "))
cantidad_numeros += 1
if numero < 0 and negativos == 0:
    negativos += numero 
while numero != 0:
    numero = int(input("Ingrese otro numero o ingrese 0 para salir: "))
    cantidad_numeros += 1
    if numero > 0:
        suma_positivos += numero
    else:
        if numero < 0 and negativos == 0:
            negativos += numero
        elif numero < 0:
            negativos = negativos * numero


print(f"El producto de los numeros negativos es: {negativos} \nLa suma de los numeros positivos es: {suma_positivos}")
'''

'''
#8) Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador_numeros = 0
menor = 0
mayor = 0

numero = int(input("Ingrese un numero: "))
menor = numero
mayor = numero
contador_numeros += 1 
while contador_numeros < 10:
    numero = int(input("Ingrese otro numero: "))
    contador_numeros += 1
    if numero < menor:
        menor = numero
    elif numero > mayor:
        mayor = numero

print(f"De los {contador_numeros} numeros ingresados el mayor es {mayor} y el menor es {menor}.")
'''

'''
#9) Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

cantidad_numeros = 0
suma_numeros = 0
almenos = 5

numero = int(input(f"Ingrese un numero, minimo numeros restantes {almenos}: "))
while numero == 0:
    numero = int(input(f"ERROR. Ingrese otro numero, minimo numeros restantes {almenos}: "))
almenos -= 1
cantidad_numeros += 1
suma_numeros += numero
while almenos > 0:
    numero = int(input(f"Ingrese otro numero, minimo numeros restantes {almenos}: "))
    while numero == 0:
        numero = int(input(f"ERROR. Ingrese otro numero, minimo numeros restantes {almenos}: "))
    almenos -= 1
    cantidad_numeros += 1
    suma_numeros += numero
while numero != 0:
    numero = int(input("Ingrese otro numero o ingrese 0 para salir: "))
    cantidad_numeros += 1
    suma_numeros += numero
    
promedio = suma_numeros / cantidad_numeros

print(f"El promedio de los {cantidad_numeros} numeros ingresados es de: {promedio}. \nLa suma de los {cantidad_numeros} numeros ingresados es de: {suma_numeros}")
'''
#9) Version FOR




'''
#10) Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

cantidad_numeros = 0
suma_numeros = 0
almenos = 5

numero = int(input(f"Ingrese un numero, minimo numeros restantes {almenos}: "))
while numero == 0:
    numero = int(input(f"ERROR. Ingrese otro numero, minimo numeros restantes {almenos}: "))
almenos -= 1
cantidad_numeros += 1
suma_numeros += numero
while almenos > 0 and cantidad_numeros < 10:
    numero = int(input(f"Ingrese otro numero, minimo numeros restantes {almenos}: "))
    while numero == 0:
        numero = int(input(f"ERROR. Ingrese otro numero, minimo numeros restantes {almenos}: "))
    almenos -= 1
    cantidad_numeros += 1
    suma_numeros += numero
while numero != 0 and cantidad_numeros <:
    numero = int(input("Ingrese otro numero o ingrese 0 para salir: "))
    cantidad_numeros += 1
    suma_numeros += numero
    
promedio = suma_numeros / cantidad_numeros

print(f"El promedio de los {cantidad_numeros} numeros ingresados es de: {promedio}. \nLa suma de los {cantidad_numeros} numeros ingresados es de: {suma_numeros}")
'''

'''
#INTEGRADOR ESTADISTICAS

#1)Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
#a) La suma acumulada de los números negativos.
#b) La suma acumulada de los números positivos.
#c) La cantidad de números negativos ingresados.
#d) El promedio de los números positivos.
#e) El número positivo más grande.
#f) El porcentaje de números negativos ingresados, respecto del total de ingresos.

cantidad_numeros = 0
cantidad_positivos = 0
cantidad_negativos = 0
suma_positivos = 0
suma_negativos = 0
mayor = False


numero = int(input("Ingrese un numero o ingrese 0 para salir: "))
while numero != 0:
    cantidad_numeros += 1
    if mayor == False:
        mayor = numero
    else:
        if numero > mayor:
            mayor = numero
    if numero > 0:
        cantidad_positivos += 1
        suma_positivos += numero
    else:
        cantidad_negativos += 1
        suma_negativos += numero
    numero = int(input("Ingrese otro numero o ingrese 0 para salir: "))

print(f"a) La suma de numeros negativos es: {suma_negativos}")
print(f"b) La suma de numeros positivos es: {suma_positivos}")
print(f"c) La cantidad de numeros negativos ingresados es: {cantidad_negativos}")
print(f"d) El promedio de los {cantidad_positivos} numeros positivos ingresados es: {suma_positivos/cantidad_positivos}")
print(f"e) El mayor numero ingresado es: {mayor}")
print(f"f) El porcentaje de los {cantidad_numeros} numeros ingresados es: {(cantidad_negativos / cantidad_numeros) * 100}")
'''


#INTEGRADOR VALIDACIONES

# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

print("Ingrese los datos del empleado.")

apellido = input("Ingrese el apellido: ")
while len(apellido) > 20:
    apellido = input("Apellido demasiado largo, intente nuevamente: ")
edad = int(input("Ingrese una edad entre 18 y 90 años: "))
while edad < 18 or edad > 90:
    edad = int(input("Edad no valida, intente nuevamente: "))
estado_civil = input("Ingrese su estado civil(Soltero/a, Casado/a, Divorciado/a o Viudo/a): ")
while estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
    estado_civil = input("Estado civil no valido, intente nuevamente: ")
legajo = int(input("Ingrese su legajo de 4 cifras, sin 0 al izquierda: "))
while legajo < 1000 or legajo > 9999:
    legajo = int(input("Legajo invalido, intente nuevamente: "))

print("Carga completada")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Legajo: {legajo}")
