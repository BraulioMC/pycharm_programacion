def separar_millar(num):
    '''
    Funcion para separar por punto cada millar en el numero introducido
    :param num: (str) de numero total introducido por usuario
    :return: (str) numero modificado con puntos cada millar
    '''
    largo_total = len(num)
    punto = largo_total - 3
    while punto > 0:
        num = (num[:punto] + "." + num[punto:])
        punto = punto - 3
    return num

def salida_comun(num, decimal, resto):
    '''
    Funcion que concatena numero con resto decimal, es la misma tanto si lleva decimal separado por punto o por coma
    en el momento que el usuario introduce el numero
    :param num: (str) parte entera del numero introducido por el usuario
    :param decimal: (int) posicion dentro del array del separador entero/decimal
    :param resto: (str) parte decimal del numero
    :return: (str) retorna el numero dividido por millares concatenado con el resto
    '''
    num = num[:decimal]
    num = (separar_millar(num))
    return (num + "," + str(resto))

def num_punto(num):
    '''
    Determina la parte entera de la parte decimal
    :param num: (str) Numero introducido por el usuario
    :return resto, decimal: (str) Parte decimal y posicion del divisor entero/decimal
    '''
    decimal = num.find(".")
    resto = num[decimal + 1:]
    return resto, decimal

def num_coma(num):
    '''
    Determina la parte entera de la parte decimal
    :param num: (str) Numero introducido por el usuario
    :return resto, decimal: (str) Parte decimal y posicion del divisor entero/decimal
    '''
    decimal = num.find(",")
    resto = num[decimal + 1:]
    return resto, decimal



def procesar_num(num):
    '''
    Funcion general para procesar el numero introducido por el usuario.
    :param num: (str) Numero introducido por el usuario
    :return: (str) Salida dividida en su parte entera por puntos y decimal por coma
    '''

    if num.find("-") != -1:
        num = num[1:]
        if num.find(".") != -1:
            resto, decimal = num_punto(num)
            print("-" + salida_comun(num, decimal, resto))

        elif num.find(",") != -1:
            resto, decimal = num_coma(num)
            print("-" + salida_comun(num, decimal, resto))

        else:
            print("-" + separar_millar(num))

    else:
        if num.find(".") != -1:
            resto, decimal = num_punto(num)
            print(salida_comun(num, decimal, resto))

        elif num.find(",") != -1:
            resto, decimal = num_coma(num)
            print(salida_comun(num, decimal, resto))

        else:
            print(separar_millar(num))
    return ""

if __name__ == "__main__":
    print(procesar_num(input("Introduce numero: ")))