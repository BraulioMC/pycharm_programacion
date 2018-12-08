def menu():
    '''Crea un menu de seleccion'''
    print("*"*20)
    print("{}{:^18}{}".format("*", "CESAR", "*"))
    print("*" * 20)
    print("{:<2}{}{:>10}".format("*", "[C]ifrar", "*"))
    print("{:<2}{}{:>7}".format("*", "[D]escifrar", "*"))
    print("{:<2}{}{:>11}".format("*", "[S]alir", "*"))
    print("*" * 20)
    return ""

print(menu())
