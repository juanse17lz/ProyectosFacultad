'''
Facturación del Servicio de Agua Potable

El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.

A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.
Tarifa base:
Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
El costo por metro cúbico (m³) de agua es de $200/m³.
Bonificaciones y Recargos según tipo de cliente:

Cliente Residencial:
Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

Cliente Comercial:
Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

Cliente Industrial:
Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

Casos especiales:
Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.

En todos los casos, se aplica el IVA del 21% sobre el total.

Requerimientos del programa:
Solicitar al usuario:
-Cantidad de metros consumidos
-Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
Calcular:
-Subtotal de consumo.
-Bonificaciones, si corresponde
-Recargos, si corresponde
-Subtotal, con recargos y bonificaciones.
-IVA aplicado (21%), si corresponde.
-Total final a pagar.
Mostrar en pantalla el desglose de los cálculos.
'''

consumido = int(input("Ingrese la cantidad de metros cubicos de agua consumidos: "))
tipo = input("Ingrese el tipo de cliente(Residecial -> a, Industrial -> b, Comercial -> c): ")
while tipo != "a" and tipo != "b" and tipo != "c":
    tipo = input("ERROR. Ingrese el tipo de cliente(Residecial -> a, Industrial -> b, Comercial -> c): ")

costo_consumido = consumido * 200
total_bruto = 7000 + costo_consumido
bonificacion = 0
recargo = 0
especial = 0
total_sin_iva = 0
final = 0

match tipo:
    case "a":
        if consumido < 30:
            bonificacion = costo_consumido * 0.1
            total_sin_iva = total_bruto - bonificacion
        elif consumido > 80:
            recargo = costo_consumido * 0.15
            total_sin_iva = total_bruto + recargo
        else:
            total_sin_iva = total_bruto
        
        if total_bruto < 35000:
            especial = total_bruto * 0.05
            total_sin_iva -= especial

        iva = total_sin_iva * 0.21
        final = total_sin_iva + iva
    case "b":
        if consumido < 200:
            recargo = costo_consumido * 0.1
            total_sin_iva = total_bruto + recargo
        elif consumido > 500:
            bonificacion = costo_consumido * 0.2
            total_sin_iva = total_bruto - bonificacion
        elif consumido > 1000:
            bonificacion = costo_consumido * 0.3
            total_sin_iva = total_bruto - bonificacion
        else:
            total_sin_iva = total_bruto    
        
        iva = total_sin_iva * 0.21
        final = total_sin_iva + iva
    case "c":
        if consumido < 50: 
            recargo = costo_consumido * 0.05
            total_sin_iva = total_bruto + recargo
        elif consumido > 150:
            bonificacion = costo_consumido * 0.08
            total_sin_iva = total_bruto - bonificacion
        elif consumido > 300:
            bonificacion = costo_consumido * 0.12
            total_sin_iva = total_bruto - bonificacion
        else:
            total_sin_iva = total_bruto

        iva = total_sin_iva * 0.21
        final = total_sin_iva + iva

print("Datos del cliente\n")
print(f"Sub-total: {total_bruto}$")
print(f"Bonificacion: {bonificacion}$")
print(f"Bonificacion especial: {especial}")
print(f"Recargo: {recargo}$")
print(f"Total sin IVA: {total_sin_iva}")
print(f"IVA: {iva}")
print(f"Precio final: {final}$")