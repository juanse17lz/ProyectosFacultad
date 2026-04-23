def buscar_datos(dnis:list,dni:int) -> int:

    indice = None
    for index in range (len(dnis)): 
        if dnis[index] == dni:
            indice = index
            break
    return indice
         
nombres = ["Mathias","Antonela","Umma","Sol","Ezequiel"]
edades = [35, 33, 13, 13, 35]
generos = ["M", "F", "X", "F", "M"]
estaturas = [1.90, 1.56, 1.56, 1.79, 1.89]  
dnis = [11111110, 11111111, 11111112, 11111113, 11111114]

while True:
    dni = int(input("Ingrese el DNI: "))
    indice= buscar_datos(dnis,dni) 
    if indice == None:
        print("DNI inexsistente")
    else:
        print("NOMBRE\t\tEDAD\tGENERO\tESTATURA\tDNI")

        if len(nombres[indice]) > 7:              
            print(f"{nombres[indice]}\t {edades[indice]}\t  {generos[indice]}\t  {estaturas[indice]}\t\t{dnis[indice]}")
        else:
            print(f"{nombres[indice]}\t\t {edades[indice]}\t  {generos[indice]}\t  {estaturas[indice]}\t\t{dnis[indice]}")
    
    continuar=input("Desea continuar?: si - no").lower()
    if continuar =="no" :
        break

