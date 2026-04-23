max_barbijos = 0
barbijos = " "
cant_barbijos = 0
cant_max = 0
item_max = " "
item_max_marca = " "
jabon_max = 0

for i in range(5):
    tipo = input("Ingrese el tipo de producto, sea barbijo, jabon o alcohol: ")
    while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
         tipo = input("ERROR\nEl tipo ingresado debe ser barbijo, jabon o alcohol: ")

    precio = int(input("Igrese el valor del producto, el valor debe de ser entre 100 y 300: "))
    while precio < 100 or precio > 300:
        precio = int(input("ERROR\nEl tipo ingresado debe encontrarse entre 100 y 300: "))

    cantidad_u = int(input("Ingrese la cantidad de unidades del producto, no debe ser menor a 1 ni superar las 1000 unidades: "))
    while cantidad_u < 1 or cantidad_u > 1000:
        cantidad_u = int(input("ERROR\nLa cantidad ingresadad no se encuentra en el rango de 1 a 1000: "))

    marca = input("Ingrese la marca y fabricante del producto: ")

    if tipo == "barbijo" and precio > max_barbijos:
            max_barbijos = precio
            barbijos = marca
            cant_barbijos += cantidad_u

    if cantidad_u > cant_max:
        cant_max = cantidad_u
        item_max = tipo
        item_max_marca = marca

    if tipo == "jabon":
        jabon_max += cantidad_u

print(f"A- Los barbijos mas caros son {barbijos}, con un precio de ${max_barbijos} y cuenta con {cant_barbijos} unidades.")
print(f"B- El item con mas unidades es {item_max}, de la marca {item_max_marca} con {cant_max} unidades.")
print(f"C- El jabon cuenta con {jabon_max} unidades.")