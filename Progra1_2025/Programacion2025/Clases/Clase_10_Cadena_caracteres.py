texto = "Python es divertido"
texto2 = texto[0:6]
texto3 = texto[7:9]
texto4 = texto[10:19]
#print(texto2,texto3,texto4)

def verificar_nombre(cadena:str)->bool:
    """Determina si en una cadena de caracteres alguno de sus digitos es un numero.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        bool: Devuelve True si contiene numeros, caso contrario devuelve False.
    """
    contiene_numero = False
    for i in cadena:
        if ord(i) >= 48 and ord(i) <= 57:
            contiene_numero = True
            break
    return contiene_numero

#print(verificar_nombre("hola  estas"))

def termino_mail(mail:str)->str:
    """Guarda la terminacion de un mail y lo devuelve. Guarda todo lo que encuentre despues del primer arroba encontrado.

    Args:
        mail (str): Cadena a verificar.

    Returns:
        str: _description_
    """
    termino = None
    contador = 0
    for i in range(len(mail)):
        if ord(mail[i]) == 64:
            termino = mail[i:len(mail)]
            contador += 1
    if termino == None or contador > 1:
        termino = "No es un mail."
    return termino 

print(termino_mail("juanselopez17@yahoo@.com"))

def verificar_mail(cadena:str,mails_validos:list)->bool:
    """Verifica si la cadena pasada es un mail o no, y si se encuentra dentro de la lista de mails validos.

    Args:
        cadena (str): Cadena de caracteres.
        list (str): Lista de mails validos.

    Returns:
        bool: Devuelve True si es un mail, caso contrario devuelve False.
    """
    es_mail = False
    for i in range(len(cadena)):
        if ord(cadena[i]) == 64:
            termino = cadena[i:len(cadena)]
            break
    for mail in range(len(mails_validos)):
        if termino == mails_validos[mail]:
            es_mail = True
            break
    if es_mail == False:
        print("Mail no valido.")
    return es_mail

lista_mails = ["@yahoo.com","@yahoo.com.ar","@hotmail.es","@hotmail.com","@outlook.com","@outlook.com.ar"]

verificacion = verificar_mail("hfgsar@hotmail.com",lista_mails)
#print(verificacion)

def mi_upper(cadena:str)->str:
    for i in range(len(cadena)):
        if ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122:
            cadena[i] = chr(ord(cadena[i])-32)


print(mi_upper("hola"))