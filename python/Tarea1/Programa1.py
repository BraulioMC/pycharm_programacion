'''
Escribe un programa que pida el número de días, horas, minutos y
segundos y calcule el número total de segundos
'''


print("CONVERSOR A SEGUNDOS")
print()
dias = int(input("Número de días: "))
horas = int(input("Número de horas: "))
minutos = int(input("Número de minutos: "))
segundos = int(input("Número de segundos: "))

tdias = dias*24*24*60
thoras = horas*24*60
tminutos = minutos*60
total = tdias + thoras + tminutos + segundos

print()
print(dias , "días, " ,
      horas , "horas, " ,
      minutos , "minutos y ",
      segundos , "segundos son " ,
      total ,"segundos"
)