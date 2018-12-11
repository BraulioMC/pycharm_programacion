num = "1234567,876868"

def separar_millar(num):
    largo_total = len(num)
    punto = largo_total - 3
    while punto > 0:
        num = (num[:punto] + "." + num[punto:])
        punto = punto - 3
    return num

def salida_comun(num, decimal):


if num.find(".") != -1:
    decimal = num.find(".")
    resto = num[decimal + 1:]
    num = num[:decimal]
    num = (separar_millar(num))
    print(num + "," + str(resto))

elif num.find(",") != -1:
    decimal = num.find(",")
    resto = num[decimal:]
    num = num[:decimal]
    num = (separar_millar(num))
    print(num + str(resto))
else:
    separar_millar(num)



