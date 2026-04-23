numero = 8

for i in range(numero, 0, -1):
    if i > 1:
        if i == numero:
            resultado = i * (i-1)
        else:
            resultado = resultado * (i-1)

print(resultado)

def calcular_factorial(numero):
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    
    return resultado
print(calcular_factorial(numero))

def sumar_naturales(numero):
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)

    return resultado

print(sumar_naturales(numero))

def calcular_potencia(base, exponente):
    if exponente == 0:
        resultado = base
    else:
        resultado = base * calcular_potencia()