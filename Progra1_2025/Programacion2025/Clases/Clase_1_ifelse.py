#1) A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o 

'''
altura = int(input("Ingrese su altura en centimetros: "))
if altura < 160:
    print("UStede jugara de Base")
elif altura > 159 and altura < 180:
    print("Usted jugara de Escolta")
elif altura > 179 and altura < 200:
    print("Usted jugara de Alero")
else:
    print("Ustede jugara de Ala-Pivot")
'''

#2) Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...
'''
contador = 0
total = 0

while contador < 3:
    nota = int(input("Ingrese una nota: "))
    while nota < 1 or nota > 10:
        nota = int(input("Nota no valida; intente nuevamente: "))
    contador += 1
    total += nota
promedio = total/contador

if promedio < 4:
    print(f"Desaprobado, su nota es {promedio}") 
elif promedio >= 4 and promedio < 7:
    print(f"Aprobado, su nota es {promedio}")
else:
    print(f"Promocionado, su nota es {promedio}")
'''

# MATCH
# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion = input("Ingese una estacion del año(Verano, Otoño, Invierno o Primavera): ")
match estacion:
    case "Verano":
        print("Se viaja a Mar del plata y Cataratas.")
    case "Otoño":
        print("Se viaja a todos los lugares.")
    case "Invierno":
        print("Solo se viaja a Bariloche.")
    case "Primavera":
        print("Se viaja a todos los lugares menos Bariloche.")
    case _:
        print("Estacion no valida.")
