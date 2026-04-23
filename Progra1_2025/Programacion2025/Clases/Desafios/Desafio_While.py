'''
 Desafío: Encuesta Tecnológica en UTN Technologies

 UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.

Las tecnologías en evaluación son:
 🔹 Inteligencia Artificial (IA)
 🔹 Realidad Virtual/Aumentada (RV/RA)
 🔹 Internet de las Cosas (IOT)

Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.

🔹 Recolección de Datos
Cada empleado encuestado deberá proporcionar la siguiente información:
 ✔️ Nombre
 ✔️ Edad (debe ser 18 años o más)
 ✔️ Género (Masculino, Femenino, Otro)
 ✔️ Tecnología elegida (IA, RV/RA, IOT)

El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.

🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    Su género no sea Femenino 
    Su edad está entre los 33 y 40 años.
3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


🔹 Requisitos del Programa
 ✔️ Los datos deben solicitarse y validarse correctamente.
 ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
 ✔️ Presentar los resultados de manera clara y organizada.
'''

print("Ingrese los datos de 10 empleado.\n")
contador_1 = 0
contador_2 = 0
empleado = 0
mayor = 0
mayor_nombre = ""
mayor_votacion = ""

for i in range(10):
    empleado += 1
    nombre = input("Ingrese el nombre: ")
    while type(nombre) != str:
        nombre = input("nombre demasiado largo, intente nuevamente: ")
    edad = int(input("Ingrese una edad entre 18 y 90 años: "))
    while edad < 18 and type(edad) != int:
        edad = int(input("Edad no valida, intente nuevamente: "))
    genero = input("Ingrese su genero(Masculino -> a, Femenino -> b o Otro -> c): ")
    while genero != "a" and genero != "b" and genero != "c" and type(genero) != str:
        genero = input("Genero no valido, intente nuevamente: ")
    tecnologia = input("Ingrese su tecnologia elegida(IA -> a, RV/RA -> b o IOT -> c): ")
    while tecnologia != "a" and tecnologia != "b" and tecnologia != "c" and type(tecnologia) != str:
        tecnologia = input("Tecnologia no valida, intente nuevamente(IA -> a, RV/RA -> b o IOT -> c): ")

    if genero == "a" and edad >= 25 and edad <= 50 and tecnologia != "b":
        contador_1 += 1
    
    if tecnologia != "a" and genero != "b" and edad >= 33 and edad <= 40:
        contador_2 += 1
        
    if edad > mayor and genero == "a":
        mayor = edad
        mayor_nombre = nombre
        match tecnologia:
            case "a":
                mayor_votacion = "IA"
            case "b":
                mayor_votacion = "RV/RA"
            case "c":
                mayor_votacion = "IOT"
    
    print(f"Carga exitosa. Empleado {empleado} cargado.\n")
porcentaje = (contador_2/empleado) * 100

print("Carga completada\n")
print(f"Empleados masculinos que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive): {contador_1} ")
print(f"Porcentaje de empleados que NO votaron por IA, no femeninos entre 33 y 40 años: {porcentaje}%")
print(f"Elmplado de masculino de mayor edad: ")
print(f"- Nombre: {mayor_nombre}")
print(f"- Edad: {mayor}")
print(f"- Tecnologia elegida: {mayor_votacion}")