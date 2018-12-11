def separar_millar(num):
    largo_total = len(num)
    punto = largo_total - 3
    while punto > 0:
        num = (num[:punto] + "." + num[punto:])
        punto = punto - 3
    return num

def salida_comun(num, decimal, resto):
    num = num[:decimal]
    num = (separar_millar(num))
    return (num + "," + str(resto))

def num_punto(num):
    decimal = num.find(".")
    resto = num[decimal + 1:]
    return resto, decimal

def num_coma(num):
    decimal = num.find(",")
    resto = num[decimal + 1:]
    return resto, decimal



def procesar_num(num):

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

print(procesar_num(input("Introduce numero: ")))