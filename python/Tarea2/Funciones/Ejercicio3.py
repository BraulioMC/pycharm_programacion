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

print(menu())
