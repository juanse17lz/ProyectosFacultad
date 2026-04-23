''' Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.'''
'''
suma = 0

cantidad = int(input("Ingrese un numero entre 5 y 10: "))

while cantidad > 10 or cantidad < 5:
    cantidad = int(input("Error: ingrese un numero entre 5 y 10: "))

for i in range(cantidad):
    n = int(input("Ingrese numeros: "))
    suma += n

promedio = suma / cantidad
print(f"El promedio es: {promedio}")
print(f"La suma es: {suma}")
'''

#1) Mostrar los números ascendentes desde el 1 al 10

'''
for i in range(10):
    print(i+1)
'''
#2) Mostrar los números descendentes desde el 10 al 1

'''
cantidad = 10
for i in range(cantidad):
    print(cantidad - i)
'''

#3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

'''
numero = int(input("Ingrese un numero: "))
for i in range(numero + 1):
    print(i)
'''

#4) Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

'''
numero = int(input("Ingrese un numero y se mostrara su tabla: "))
for i in range(10):
    print(f"{i+1} x {numero} = {numero * (i+1)}")
'''

#5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

'''
acumulador = 0
for i in range(10):
    numero = int(input("Ingrese un numero o ingrese 0 para salir: "))
    if numero == 0:
        break
    else:
        acumulador += numero
print(f"La suma de los numeros ingresados es: {acumulador}")
'''

#6) Imprimir los números múltiplos de 3 entre el 1 y el 10.

'''
for i in range(10):
    if (i+1)%3 == 0:
        print(i+1)
'''

#7) Mostrar los números pares que hay desde la unidad hasta el número 50.

'''
for i in range(50):
    if (i+1)%2 == 0:
        print(i+1)
'''

#8) Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente

'''
numero = int(input("Ingrese un numero: "))
lista = []

for i in range(numero):
    lista += [i+1]
    for j in lista:
        print(j, end="")
    print("")
'''

#9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

'''
numero = int(input("Ingrese un numero: "))
for i in range(numero):
    if numero%(i+1) == 0:
        print(i+1)
'''

#10) Ingresar un número. Determinar si el número es primo o no.

'''
contador = 0
numero = int(input("Ingrese un numero: "))
for i in range(numero):
    if numero%(i+1) == 0:
        contador += 1
if contador > 2:
    print("El numero no es primo.")
else:
    print("El numero es primo.")
'''

#11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.


primos = 0
numero = int(input("Ingrese un numero: "))
for j in range(numero):
    contador = 0
    for i in range(j+1):
        if (j+1) % (i+1) == 0:
            contador += 1
    if contador == 2:
        print(j+1)
        primos += 1
print(f"La cantidad de primos encontrados es: {primos}")
