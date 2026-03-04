dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el anio: "))

dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
if mes < 1 or mes > 12:
    print ("Mes invalido")
    exit()

if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 = 0):
    dias_mes[1] = 29

dia += 1

if dia > dias_mes[mes -1]:
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        anio += 1

print("Nueva fecha:", dia, "/", mes, "/", anio)
print ("Modificacion hecha en el repositorio")
