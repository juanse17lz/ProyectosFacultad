def calcular_edad(año_actual,mes_actual,dia_actual,año_nacimiento,mes_nacimiento,dia_nacimiento):
    dia = dia_actual - dia_nacimiento
    if dia < 1:
        mes_nacimiento -= 1
    mes = mes_actual - mes_nacimiento
    if mes < 1:
        año_nacimiento -= 1
    edad = año_actual - año_nacimiento
    return edad

"""
año_actual = int(input("Ingrese el año actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
dia_actual = int(input("Ingrese el dia actual: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))
dia_nacimiento = int(input("Ingrese su dia de nacimiento: "))
print(calcular_edad(año_actual,mes_actual,dia_actual,año_nacimiento,mes_nacimiento,dia_nacimiento))
"""

def tipo_vehiculo(patente:str)->str:  
    for i in patente: 
        if ord(i) >= 65 and ord(i) <= 90:
            vehiculo = "Auto"                
        else:
            vehiculo = "Moto"
        break    
    return vehiculo
            
"""
tipo_de_vehiculo = input("Ingrese la patente del vehiculo: ")
print(tipo_vehiculo(tipo_de_vehiculo))
"""

def cuil_cuit(dni,tipo):
    suma = 0
    cont_dni = 0

    if tipo == "MASCULINO":
        tipo = "20"
    elif tipo == "FEMENINO":
        tipo = "27"
    else:
        tipo = "30"

    for i in tipo:
        if suma == 0:
            suma += int(i) * 5
        else:
            suma += int(i) * 4

    for i in dni:
        if cont_dni == 0:
            suma += int(i) * 3
            cont_dni += 1
        elif cont_dni == 1:
            suma += int(i) * 2
            cont_dni += 1
        elif cont_dni == 2:
            suma += int(i) * 7
            cont_dni += 1
        elif cont_dni == 3: 
            suma += int(i) * 6
            cont_dni += 1
        elif cont_dni == 4:
            suma += int(i) * 5
            cont_dni += 1
        elif cont_dni == 5:
            suma += int(i) * 4
            cont_dni += 1
        elif cont_dni == 6:
            suma += int(i) * 3
            cont_dni += 1
        elif cont_dni == 7:
            suma += int(i) * 2
            cont_dni += 1

    resultado = suma/11
    resto = suma - (resultado*11)

    if resto == 0:
        z = 0
    elif resto == 1:
        if tipo == 20:
            tipo = 23
            z = 9
        elif tipo == 27:
            tipo = 23
            z = 4
    else:
        z = 11 - resto
    
    cuit_cuil = print(f"Su CUIL/CUIT es: {tipo}-{dni}-{z}")
    return cuit_cuil

"""
ingrese_tipo = input("Ingrese segun corresponda (MASCULINO|FEMENINO|EMPRESA): ")
ingrese_dni = input("Ingrese su dni: ")
cuil_cuit(ingrese_dni,ingrese_tipo)
"""