def validate_number(cadena)->bool:
    for i in cadena:
        if ord(i) > 47 and ord(i) < 58:
            flag = True
        else:
            flag = False
            break
    return flag

print(validate_number("456871354841q"))

