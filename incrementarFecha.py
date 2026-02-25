dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el anio: "))

dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 = 0):
    dias_mes[1] = 29

dia += 1

if data > dias_mes[mes -1]:
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        anio += 1

print("Nueva fecha:", dia, "/", mes, "/", anio)