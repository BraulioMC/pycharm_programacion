def menu():
    '''Crea un menu de seleccion'''
    print("*"*22)
    print("{}{:^20}{}".format("*", "C E S A R", "*"))
    print("*" * 22)
    print("{:<2}{}{:>12}".format("*", "[C]ifrar", "*"))
    print("{:<2}{}{:>9}".format("*", "[D]escifrar", "*"))
    print("{:<2}{}{:>13}".format("*", "[S]alir", "*"))
    print("*" * 22)
    return ""

def cesar(texto, clave):
    '''Cifrado cesar'''

    crypto_msg = ""
    texto = texto.upper()
    for i in texto:
        if i >= "A" and i <= "Z":
            crypto_ascii = ord(i) + clave

            if crypto_ascii < ord("A"):
                crypto_ascii += 26
            elif crypto_ascii > ord("Z"):
                crypto_ascii -= 26

            crypto_msg += chr(crypto_ascii)
        else:
            crypto_msg += i
    return crypto_msg

print(menu())

opcion_menu =