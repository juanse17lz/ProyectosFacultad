"""set = {3,1,2,4,5,6,1,4,6,10,11}
print(type(set))
print(set)

set_2 = {10,12,11,15}

interseccion = set.intersection(set_2)

print(interseccion)

mi_lista = [1,8,3,6,5]
print(type(mi_lista))
print(mi_lista)
mi_lista[1] = 2
print(mi_lista)

mi_tupla = tuple(mi_lista)
print(mi_tupla)"""
#mi_tupla[1] = 8

alumnos = [
    {
        'nombre':"Alvaro Angulo",
        'genero': "M",
        'edad': 28,
        'legajo': 7777,
        'materia_1': 7,
        'materia_2': 7,
        'materia_3': 7,
        'materia_4': 7,
        'materia_5': 7,
        'promedio': 7
    },
    {
        'genero': "M",
        'edad': 28,
        'nombre':"Walter Cozzani",
        'legajo': 6587,
        'materia_1': 8,
        'materia_2': 5,
        'materia_3': 6,
        'materia_4': 3,
        'materia_5': 8}]

def imprimir_alumno(alumno:dict):
    print(alumno['nombre'])

def recorrer_datos(datos_alumnos:list):
    for alumno in datos_alumnos:
        imprimir_alumno(alumno)

def buscar_alumno(datos_alumnos:list,legajo:int)->dict:
    retorno = {'genero': "",
        'edad': 0,
        'nombre':"",
        'legajo': 0,
        'materia_1': 0,
        'materia_2': 0,
        'materia_3': 0,
        'materia_4': 0,
        'materia_5': 0}
    for alumno in datos_alumnos:
        if legajo == alumno['legajo']:
            retorno = alumno
            break
    return retorno

imprimir_alumno(buscar_alumno(alumnos,6587))
